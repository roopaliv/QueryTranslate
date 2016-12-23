import web
from mtranslate import translate
import urllib
import json

urls = (
  '/hello', 'Index'
)
app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):

    def GET(self):
        form = web.input(pagesize="10", query="trump", pageno="1", language="all")
        #greeting = "%s, %s" % (form.greet, form.name)
	to_translate=(form.query).encode('utf8')
	str1=translate(to_translate)+' '+translate(to_translate, 'es')+' '+translate(to_translate, 'hi')+' '+translate(to_translate, 'de')+' '+translate(to_translate, 'ja')+' '+translate(to_translate, 'ru')+' '+translate(to_translate, 'ar')+' '+translate(to_translate, 'it')+' '+translate(to_translate, 'fr')+' '+translate(to_translate, 'ur')
	words = set()
	result = ''
	for word in str1.split():
	    if word not in words:
	        result = result + word +' '
	        words.add(word)
	    else:
		words.remove(word)
	url1=urllib.quote(result.encode('utf8'));
	ps=form.pagesize
	pn=int(form.pageno)
	ps1=int(ps)
	pn-=1
	ps1*=pn
	ps1+=1
	#print ps1
	#startno=str(ps1*(pn-1)+1)
	if form.language=="all":
		data = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
		countdata=urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	else:
		data = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:'+form.language+'&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
		countdata=urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:'+form.language+'&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	totalcount=json.load(countdata)['response']['numFound']
	docs = json.load(data)['response']['docs']
	web.header('Content-Type', 'application/json')
	data2 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:en&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	data3 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:es&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	data4 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:hi&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	data5 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:de&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	data6 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:ja&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	data7 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:ru&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	data8 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:ar&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	data9 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:it&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	data10 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:fr&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	data11 = urllib.urlopen('http://35.163.101.223:8984/solr/IRPROJECT4/select?q='+url1+'&fl=tweet_id%2Cuser_id%2Ctweet_lang&wt=json&indent=true&rows='+ps+'&start='+str(ps1)+'&defType=edismax&fq=tweet_lang:ur&qf=text_en^2%20text_en_lower%20text_es^2%20text_de^2%20text_hi^2%20text_ja^2%20text_ru^2%20text_ar^2%20text_it^2%20text_fr^2%20text_ur^2')
	docs2 = json.load(data2)['response']['numFound']
	docs3 = json.load(data3)['response']['numFound']
	docs4 = json.load(data4)['response']['numFound']
	docs5 = json.load(data5)['response']['numFound']
	docs6 = json.load(data6)['response']['numFound']
	docs7 = json.load(data7)['response']['numFound']
	docs8 = json.load(data8)['response']['numFound']
	docs9 = json.load(data9)['response']['numFound']
	docs10 = json.load(data10)['response']['numFound']
	docs11 = json.load(data11)['response']['numFound']
	langcount={'en':docs2,'es':docs3,'hi':docs4,'de':docs5,'ja':docs6,'ru':docs7,'ar':docs8,'it':docs9,'fr':docs10,'ur':docs11}
	finaljson={'totalcountinfo':totalcount,'languageData':langcount,'results':docs}
	web.header('Access-Control-Allow-Origin',      '*')
	web.header('Access-Control-Allow-Credentials', 'true')
	return json.dumps(finaljson)

if __name__ == "__main__":
    app.run()