import os, json, urllib.request, datetime, pathlib, html
owner = os.environ.get("PROFILE_OWNER", "Velazquez-karellen")
token = os.environ["GITHUB_TOKEN"]
query = """query($login:String!,$from:DateTime!,$to:DateTime!){user(login:$login){followers{totalCount} repositories(privacy:PUBLIC,ownerAffiliations:OWNER){totalCount} contributionsCollection(from:$from,to:$to){contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}"""
now = datetime.datetime.now(datetime.timezone.utc)
start = now - datetime.timedelta(days=364)
req = urllib.request.Request("https://api.github.com/graphql", data=json.dumps({"query":query,"variables":{"login":owner,"from":start.isoformat(),"to":now.isoformat()}}).encode(), headers={"Authorization":"Bearer "+token,"Content-Type":"application/json","User-Agent":"orbit-profile"})
with urllib.request.urlopen(req, timeout=30) as response:
    data = json.load(response)
if data.get("errors"):
    raise RuntimeError(data["errors"])
user = data["data"]["user"]
calendar = user["contributionsCollection"]["contributionCalendar"]
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="210" viewBox="0 0 1000 210"><rect width="1000" height="210" rx="10" fill="#060b14"/>']
for i,(label,value) in enumerate([("Public repositories",user["repositories"]["totalCount"]),("Contributions",calendar["totalContributions"]),("Followers",user["followers"]["totalCount"])]):
    x=12+i*330
    parts.append(f'<rect x="{x}" y="10" width="316" height="68" rx="8" fill="#101d30" stroke="#234c78"/><text x="{x+15}" y="38" fill="#59c7ef" font-family="monospace" font-size="23">{value}</text><text x="{x+15}" y="60" fill="#e1ebf7" font-family="Arial" font-size="14">{label}</text>')
colors=["#15253a","#23476a","#3279a3","#59c7ef","#b5efff"]
for x,week in enumerate(calendar["weeks"]):
    for day in week["contributionDays"]:
        y=(datetime.date.fromisoformat(day["date"]).weekday()+1)%7
        n=day["contributionCount"]
        level=0 if n==0 else 1 if n<3 else 2 if n<6 else 3 if n<10 else 4
        parts.append(f'<rect x="{15+x*18}" y="{88+y*14}" width="12" height="11" rx="2" fill="{colors[level]}"><title>{day["date"]}: {n}</title></rect>')
parts.append(f'<text x="15" y="199" font-family="monospace" font-size="11" fill="#a5bed7">GITHUB ACTIVITY / UPDATED {now.date()} UTC / API-visible contributions</text></svg>')
pathlib.Path("assets/components/github-activity.svg").write_text("".join(parts),encoding="utf-8")
