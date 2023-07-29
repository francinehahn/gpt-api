<h1 align="center">API REST using OpenAI API</h1>

## ℹ️About
This is an API REST that consumes data from the OpenAI API.

## 👩‍💻 Technologies used
- Python
- Flask
- OpenAI API
- Bcrypt
- JWT
- Marshmallow
- MySQL

## 🌐 Deploy
https://gpt-api-delta.vercel.app

## ☑️ Requests
- `POST Signup: https://gpt-api-delta.vercel.app/signup`
Body:
<pre>
    <code>
        {
            "user_name": "Lucas Viana",
            "email": "lucas_viana@hotmail.com",
            "phone": "51982521177",
            "password": "12345678"
        }
    </code>
</pre>

- `POST Login: https://gpt-api-delta.vercel.app/login`
This request will return an auth token that should be used in all the other requests.
Body:
<pre>
    <code>
        {
            "email": "lucas_viana@hotmail.com",
            "password": "12345678"
        }
    </code>
</pre>


- `POST Create A Summary: https://gpt-api-delta.vercel.app/create-summary`
The user provides the auth token and a text and the endpoint returns a summary of it.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

Body:
<pre>
    <code>
        {
            "text": "A vitamina D é uma vitamina essencial para o equilíbrio de cálcio e fósforo no organismo, ajudando a evitar a osteoporose, além de fortalecer o sistema imunológico, prevenir a diabetes e manter a saúde do coração. A vitamina D é produzida no organismo na forma da vitamina D3 (colecalciferol), através da exposição à luz solar, mas também pode ser obtida com consumo de alimentos de origem animal, como peixes e ovos. Já na forma da vitamina D2 (ergocalciferol), essa vitamina está presente em suplementos, alimentos fortificados e alguns vegetais e fungos. A deficiência de vitamina D pode causar osteomalácia e osteoporose nos adultos, e raquitismo, nas crianças. Já o excesso dessa vitamina no organismo pode provocar  falta de apetite,    dor abdominal, pressão alta e fraqueza muscular."
        }
    </code>
</pre>

- `POST Create A Recipe: https://gpt-api-delta.vercel.app/create-recipe`
The user provides the ingredients and the endpoint returns a recipe.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

Body:
<pre>
    <code>
        {
            "ingredients": "frango, tomate, cebola, milho, batata, curry, leite de coco"
        }
    </code>
</pre>

- `POST Create Translation: https://gpt-api-delta.vercel.app/create-translation`
The user provides the source language, the target language and the text to be translated.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

Body:
<pre>
    <code>
        {
            "source_language": "português",
            "target_language": "inglês",
            "text": "Olá mundo!"
        }
    </code>
</pre>

- `POST Create A Text: https://gpt-api-delta.vercel.app/create-text`
The user provides the subject of the text and the endpoint returns the text.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

Body:
<pre>
    <code>
        {
            "text": "Blog post sobre os benefícios da vitamina D"
        }
    </code>
</pre>

- `GET Get Recipes By User Id: https://gpt-api-delta.vercel.app/get-recipes`
This request returns all the recipes registerd in the user account.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

- `GET Get Summaries By User Id: https://gpt-api-delta.vercel.app/get-summaries`
This request returns all the summaries registerd in the user account.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

- `GET Get Translations By User Id: https://gpt-api-delta.vercel.app/get-translations`
This request returns all the translations registerd in the user account.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

- `GET Get Texts By User Id: https://gpt-api-delta.vercel.app/get-texts`
This request returns all the texts registerd in the user account.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

- `DELETE Delete Recipe By Id: https://gpt-api-delta.vercel.app/delete-recipe/:recipe_id`
This request deletes a recipe from the account.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

Path params:
<pre>
    <code>
        {
            "recipe_id": "432d3886-f796-4658-a03b-63f855f60e00"
        }
    </code>
</pre>

- `DELETE Delete Summary By Id: https://gpt-api-delta.vercel.app/delete-summary/:summary_id`
This request deletes a summary from the account.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

Path params:
<pre>
    <code>
        {
            "summary_id": "432d3886-f796-4658-a03b-63f855f60e00"
        }
    </code>
</pre>

- `DELETE Delete Text By Id: https://gpt-api-delta.vercel.app/delete-text/:text_id`
This request deletes a text from the account.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

Path params:
<pre>
    <code>
        {
            "text_id": "432d3886-f796-4658-a03b-63f855f60e00"
        }
    </code>
</pre>

- `DELETE Delete Translation By Id: https://gpt-api-delta.vercel.app/delete-translation/:translation_id`
This request deletes a translation from the account.
Headers:
<pre>
    <code>
        {
            "Authorization": Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDU2Njc3NywianRpIjoiNDQ2ZTIzNWYtZTJiOS00OWI3LTllNzctMTA2ZGNhOGZjNzdhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjhhODU1NzNiLTJlYTItNDNhNC05YzhkLTkxYjk1OWU2ZGEzYyIsIm5iZiI6MTY5MDU2Njc3NywiZXhwIjoxNjkwNjUzMTc3fQ.F91Kouw9VHZRVga4iHTJcUSbtEAd_oVgcI4Ycgilr-o
        }
    </code>
</pre>

Path params:
<pre>
    <code>
        {
            "translation_id": "432d3886-f796-4658-a03b-63f855f60e00"
        }
    </code>
</pre>

