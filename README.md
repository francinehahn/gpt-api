<h1 align="center">API REST using OpenAI API</h1>

## ℹ️About
This is an API REST that consumes data from the OpenAI API.

## 👩‍💻 Technologies used
- Python
- Flask
- OpenAI API

## ☑️ Requests
- `Create Recipe:` The user provides the ingredients and the endpoint returns a recipe.
<pre>
    <code>
        {
            "ingredients": "frango, tomate, cebola, milho, batata, curry, leite de coco"
        }
    </code>
</pre>

- `Create A Summary:` The user provides a text and the endpoint returns a summary of it.
<pre>
    <code>
        {
            "text": "História do titanic"
        }
    </code>
</pre>

- `Translator:` The user provides the source language, the target language and the text to be translated.
<pre>
    <code>
        {
            "source_language": "português",
            "target_language": "inglês",
            "text": "Olá mundo!"
        }
    </code>
</pre>

- `Writing Assistant:` The user provides the subject of the text and the endpoint returns the text.
<pre>
    <code>
        {
            "text": "Blog post sobre os benefícios da vitamina D"
        }
    </code>
</pre>

