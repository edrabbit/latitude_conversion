import argparse
import datetime
import json
import pytz


def write_out(outf, line):
    logline = ('{ "timestamp": "%s"' % line['timestamp'])
    for k, v in line.iteritems():
        if k != 'timestamp':
            if not v:
                logline = '%s, "%s": ""' % (logline, k)
            else:
                logline = '%s, "%s": "%s"' % (logline, k, v)
    outf.write('%s}\n' % logline)

def process_file(infile, outf):
    '''infile is a path, outf is a file object'''

    dj = json.load(open(infile))
    locations = dj["locations"]
    locations.reverse()
    line = {}
    for x in locations:
        ts = (
            pytz.UTC.localize(
                datetime.datetime.fromtimestamp(int(x["timestampMs"]) / 1000)))
        line['timestamp'] = ts.isoformat()
        line['latitude'] = float(x["latitudeE7"]) / 10000000
        line['longitude'] = float(x["longitudeE7"]) / 10000000
        line['accuracy'] = x["accuracy"]
        write_out(outf, line)

def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert Latitude json data into Splunk friendly json')
    parser.add_argument(
        '-i', '--input', type=str, help='File to read', default='.')
    parser.add_argument(
        '-o', '--output', type=str, help='File to write to',
        default='output.log')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    outf = open(args.output, 'a')
    print 'Processing %s' % args.input
    process_file(args.input, outf)
    outf.close()
