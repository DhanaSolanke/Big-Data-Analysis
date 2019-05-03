import requests as req
import json
from cStringIO import StringIO
import warc

json_response = req.get("https://index.commoncrawl.org/CC-MAIN-2019-13-index?url=https%3A%2F%2Fwww.nimh.nih.gov%2F*&output=json")
pages = [json.loads(m) for m in json_response.content.strip().split('\n')]
dwarc = []


for i in range(0, 3737):
    page = pages[i]
    offset, length = int(page['offset']), int(page['length'])
    offset_end = offset + length - 1
    resp = req.get('https://commoncrawl.s3.amazonaws.com/' + page['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)},stream = True)
    buf = StringIO(resp.raw.read())
    dwarc.append(warc.WARCFile(fileobj=buf, compress=True))


def getwarcdata(warc_file, header, value):
    for record, _, _ in warc_file.browse():
        if record.header.get(header) == value:
            return record

urls = set()

for datawarc in dwarc:
    rec = getwarcdata(datawarc, header='WARC-Type', value='response')
    url_link = rec.header['WARC-Target-URI']
    urls.add(url_link)

with open('urlfiles.txt', 'a') as f:
    for each in urls:
        f.write(each+"\n")