import tweepy
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from time import sleep

ckey ='VY2Ccr2WBRtf6yPEOuxnGV0pG'
csecret ='AB04PSg3wwVfjNGtRCkgtE642mRRePdv1mP9DGIKIAacwWG4vP'
atoken ='2570689932-uKOQYYJytFhKNFsOwZ97ZcMDfqTzDm4N4aQdWm2'
asecret='iw9HPxThqHvivwScdq3fsjygVjBmXSx8VkGr7BijPALP9'
length=0
Feed=[]
ratings=[]
Countries=[['Germany','#germany','#Germany'],['Brazil','brasil'],['Italy','#Italy','#italy','italy'],['Netherland','Dutchmen','dutchmen','Holland','#Holland','#Netherlands'],['england','#england','#England','England','Lions','#ENG'],['#URU','#Uruguay','Uruguay']]
ratings=[0,0,0,0,0,0]
class listener(StreamListener):
	def search_text(self,curr_dat,flag):
		check=0
		for item in curr_dat:
			item=item.strip(' ');
			if item in ['FIFA' , 'FIFA2014' , 'World' , 'Cup' , '#fifa' , '#Fifa', '#Brazil' , '#WorldCup' , '#worldcup' , '#brazil' , 'world'] :
				check =1
				break
		if (check == 1):
			for item in curr_dat:
				print item
				j=0
				for words in Countries :
					if(item in words):
						ratings[j]=ratings[j]+flag
					j=j+1
		print 'fucker'
	def on_data(self,data):
		try:
			#print data
			tweet=data.split(',"text":"')[1].split('","source')[0]
			saveThis=str(time.time())+'::'+tweet
			saveFile=open('data.csv','a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			if(len(Feed)>=1000):
				self.search_text(Feed.pop(),-1)
			Feed.insert(0,tweet.split())
			self.search_text(Feed[0],1)
			print ratings
			return True
		except BaseException, e:
			print 'failed ondata,' ,str(e)
		time.sleep(5)
	def on_error(self,status):
		print "error"
		
auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream=Stream(auth,listener()) 	
twitterStream.filter(track=["FIFA2014",'Germany','Brazil','Italy','Netherland',"World Cup"])
