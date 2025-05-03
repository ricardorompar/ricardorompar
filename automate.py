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
    news_text = '\n<ol>'
    for i, item in enumerate(news):
        #print(f"[{i+1}]", item['title'])
        if 'url' in item:
            news_text += f'''
<li>
    <a href={item['url']} target="_blank">
        {item['title']} |
    </a>
    By: {item['by']}
</li>
'''
        if 'text' in item:
            news_text += f'''
<p>
Text: {item['text']} </br>
</p>
'''
        #for loop ends here
    date = f" {datetime.date.today().strftime('%a %d %b %Y')}"

    return date + '</h4>' + news_text + '</ol>'


def update_readme(new_text:str, file_path:str) -> None:
    insert_after = "<h4>Check the latest news from:"

    # Read the file content
    with open(file_path, "r") as file:
        content = file.read()

    # Check if the anchor exists and insert the new content
    if insert_after in content:
        parts = content.split(insert_after)
        updated_content = parts[0] + insert_after + new_text
    else:
        # If the anchor is not found, append the new content at the end
        updated_content = content + new_text

    #content back to the file:
    with open(file_path, "w") as file:
        file.write(updated_content)

if __name__ == '__main__':
    text = create_html(top_news(top_ids()))
    update_readme(text, "./README.md")