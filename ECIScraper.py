from bs4 import BeautifulSoup as bs
import httplib


class ECIScrapper:
	def __init__(self, url):
		self.url = url.split("/")[0]
		self.getrequest = '/'.join(url.split('/')[1:])
		print self.url, self.getrequest
		self.connection = httplib.HTTPConnection(self.url)
		self.connection.request("GET", '/'+self.getrequest)
		self.response = self.connection.getresponse()
		self.page = self.response.read()

		self.soup = bs(self.page)
		print self.soup.find_all('table', style="margin: auto; width: 100%; font-family: Verdana; border: solid 1px black;font-weight:lighter")

		style = "margin: auto; width: 100%; font-family: Verdana; border: solid 1px black;font-weight:lighter"


	
	def getData(self):
		print url;




if __name__=="__main__":
	url = "eciresults.ap.nic.in/ConstituencywiseS2653.htm?ac=53"
	ECIScrapper(url)
