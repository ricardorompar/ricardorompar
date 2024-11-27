import requests
import json
import datetime

#Get top news ids:
def top_ids(url='https://hacker-news.firebaseio.com/v0/topstories.json'):
    ids = requests.get(url)
    ids = json.loads(ids.text)  #transform to dict
    return ids[:5]  #return first 5 ids

#Get top news from ids:
def top_news(top_ids:list) -> list:
    items = []
    for id in top_ids:
        url_for_item = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        news_item = requests.get(url_for_item)
        news_item = json.loads(news_item.text)  #transform to dict
        items.append(news_item)

    return items

#Generate some HTML to import in the readme
def create_html(news:list) -> str:
    news_text = ''
    for i, item in enumerate(news):
        #print(f"[{i+1}]", item['title'])
        if 'url' in item:
            news_text += f'''
<a href={item['url']}>
    <h3>
        {i+1}. {item['title']} |
    </h3>
</a> </br>
'''
        if 'text' in item:
            news_text += f'''
<p>
Text: {item['text']} </br>
</p>
'''
        #for loop ends here
    date = f'''
<p>
    Date: {datetime.date.today().strftime('%a %d %b %Y')}
</p> </br>
'''

    return date + news_text


def update_readme(new_text:str, file_path:str) -> None:
    insert_after = "<h2>Today's top <a href='https://news.ycombinator.com/'>Hacker News</a></h2>"

    # Read the file content
    with open(file_path, "r") as file:
        content = file.read()

    # Check if the anchor exists and insert the new content
    if insert_after in content:
        parts = content.split(insert_after)
        updated_content = parts[0] + insert_after + "</br>" + new_text + parts[1]
    else:
        # If the anchor is not found, append the new content at the end
        updated_content = content + "</br>" + new_text

    #content back to the file:
    with open(file_path, "w") as file:
        file.write(updated_content)

if __name__ == '__main__':
    text = create_html(top_news(top_ids()))
    update_readme(text, "./README.md")