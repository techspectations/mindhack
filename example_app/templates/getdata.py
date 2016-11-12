import urllib2, json
import pickle
import summarize
import mtranslate
import re
import string
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def fetchData(url):
	req = urllib2.Request(url)
	req.add_header('Authorization', '3343965e-5704-56b2-a27c-4f2bec78d44c')
	resp = urllib2.urlopen(req)
	content = resp.read()
	content = json.loads(content)
	return content
content = fetchData("https://developer.manoramaonline.com/api/editions/en/sections")
print content['sections']
for section in content['sections']:
	print section['code']

'''array=[]
articles = fetchData("https://developer.manoramaonline.com/api/editions/en/sections/entertainment_entertainment-news/articles")
for article in articles['articleSummary']:
	array.append(article['title'])
	print article['title']
	articleData=fetchData(article['articleURL'])
	txt =summarize.summarize_text(articleData['content']).summaries[0]
	array.append(txt)
	txt=cleanhtml(txt)
	txt=txt.encode('ascii', 'ignore').decode('ascii')
	print txt
	#tr=mtranslate.translate(txt,"ml","auto")

	print "\n"
pickle.dump(array,open( "data.sav", "wb" ));
'''
