import praw
import time
import re
import MySQLdb
import bot #credentials
import anaApi 

userAgent = bot.uAgent();
un = bot.un();
pwd = bot.pwd();

r = praw.Reddit(userAgent)
r.login(un, pwd);

print "Succesfully Logged In."

actPhrase = "Yo romiseBot:"
setPhrase = "-stahpPlsNoMore"

db = bot.db()
cur = db.cursor()
print "Connected to db."
while True:
	subreddit = r.get_subreddit('UMW_CPSC470Z')
	for submission in subreddit.get_hot():
		casify = True
		cur.execute("SELECT id FROM submission WHERE id = %s", (submission.id))
		if not cur.fetchone() and submission.author.name != un:
			activate = False
			if re.search(actPhrase, submission.title, re.IGNORECASE):
				txt = re.match(actPhrase+'(.*)', submission.title, re.IGNORECASE)
				activate = True
			elif re.search(actPhrase, submission.selftext, re.IGNORECASE):
				txt = re.match(actPhrase+'(.*)', submission.selftext, re.IGNORECASE)
				activate = True
			if activate:
				txt = re.escape(txt.group(1))
				if txt.find(setPhrase) is 0:
					casify = False
					txt = txt.replace(setPhrase, '')
				submission.add_comment(anaApi.anagram(txt,casify))
				cur.execute("INSERT INTO submission (id) VALUES (%s)", submission.id)
				db.commit()
				print "Saved submission.id"
		flat_comments = praw.helpers.flatten_tree(submission.comments)
		for cmt in flat_comments:
			casify = True
			cur.execute("SELECT id FROM comments WHERE id = %s", (cmt.id))
			if re.search(actPhrase, cmt.body, re.IGNORECASE) and not cur.fetchone() and cmt.author.name != un:
				txt = re.match(actPhrase+'(.*)', cmt.body, re.IGNORECASE)
				#txt = re.escape(txt.group(1))
				txt = txt.group(1)
				if txt.find(setPhrase) is 0:
					casify = False
					txt = txt.replace(setPhrase, '')
				cmt.reply(anaApi.anagram(txt,casify))
				cur.execute("INSERT INTO comments (id) VALUES (%s)", cmt.id)
				db.commit()
				print "Saved comments.id"
			
	time.sleep(500)
cur.close()
db.close()

