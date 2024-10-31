# 🌐 Projeto Django de Aprendizado

Este é um projeto simples para aprender e explorar os fundamentos do framework Django! Aqui você encontrará um passo a passo para iniciar e configurar um projeto Django com uma aplicação básica de catálogo de empregos.

# 📝 Passo a Passo

#### 1. Criar o ambiente virtual
```bash
virtualenv env
```

#### 2. Ativar o ambiente virtual
```bash
source ./env/bin/activate
```

#### 3. Instalar Django
```bash
pip install django
```
ou instale a partir de um arquivo `requirements.txt` (se disponível):
```bash
pip install -r requirements.txt
```

#### 4. Criar o projeto Django
```bash
django-admin startproject app .
```

#### 5. Criar o app `jobs`
```bash
python manage.py startapp jobs
```
Adicione a lógica no arquivo `jobs/models.py`.

#### 6. Adicionar `jobs` às configurações do projeto

No arquivo `settings.py`, inclua `'jobs'` na lista de `INSTALLED_APPS`.

#### 7. Criar e aplicar migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 8. Criar a view para o app `jobs`

No arquivo `jobs/views.py`, defina as views necessárias.

#### 9. Criar os templates
Formulário: `jobs/templates/jobs/form.html`
Página principal: `jobs/templates/jobs/index.html`

#### 10. Configurar URLs
No arquivo `jobs/urls.py`, configure as rotas para as views.
Importe as URLs do `jobs/urls.py` no arquivo `app/urls.py`.

#### 11. Rodar o servidor
```bash
python manage.py runserver
```