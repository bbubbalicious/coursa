import urllib
import re
import time

link = 'https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19S&subj_area_cd=CHEM%20%20%20&crs_catlg_no=0172%20%20%20%20&class_id=142730200&class_no=%20001%20%20'
# link = "https://sa.ucla.edu/ro/Public/SOC/Results/ClassDetail?term_cd=19S&subj_area_cd=MATH%20%20%20&crs_catlg_no=0061%20%20%20%20&class_id=262268200&class_no=%20001%20%20"
while 1:
	info = urllib.urlopen(link).read()
	closedSearch = re.search("Closed: Class Full \([0-9]*\)", info)
	openSearch = re.search("Open: ([0-9]*) of [0-9]* Left", info)
	if closedSearch:
		pass
	elif openSearch:
		print str(int(openSearch.group(1))) + " spots left open"
	else:
		waitlistOpenSearch = re.search('([0-9]*) of ([0-9]*) Taken', info)
		if waitlistOpenSearch:
			print str(int(waitlistOpenSearch.group(2)) - int(waitlistOpenSearch.group(1))) + " spots left on waitlist"
	time.sleep(5)
