#  Desafio Django:  Correção de Bugs

## 📋 Resumo das Correções

| # | Categoria | Problema Identificado | Solução Aplicada |
|:---:|---|---|---|
| **01** | Configuração (`settings.py`) | App `portal` não declarada em `INSTALLED_APPS` | Adicionado `'portal'` à lista de aplicações instaladas |
| **02** | Roteamento (`urls.py`) | Falta do `path` com `include()` para as rotas do portal | Mapeada a rota com `include('portal.urls')` para a home e páginas filhas |
| **03** | Model Admin (`admin.py`) | Atributo inexistente (`especialidade`) listado em `list_display` | Removido o campo não herdado pelo model `Professor` |
| **04** | Forms / Models | Ausência dos campos preenchíveis `observacao` e `imagem` | Inclusão das strings dos campos no formulário/model |
| **05** | Imports / Utilitários | Falta da importação do utilitário de fuso horário | Adicionado `from django.utils import timezone` |
| **06** | Model / ORM | Ausência de `unique=True` para o campo `matricula` | Inclusão de `unique=True` por se tratar de um campo de dados irreplicável |
| **07** | Templates / Views | Redundância no caminho (`template/...`) dentro do `render()` | Removido o prefixo `template/`, usando caminho relativo |
| **08** | Views / Fallback | Tentativa de renderização de template inexistente | Criada view de fallback/temporária para referenciar o conteúdo esperado |

---

## Detalhamento dos Erros e Soluções

### 1. Ausência da Aplicação no `INSTALLED_APPS`
* **Local:** `settings.py`
* **Problema:** A aplicação `portal` não estava registrada na lista de apps instaladas, impedindo o Django de carregar seus models, migrações, rotas e templates.
* **Correção:** Adicionada a string `'portal'` na tupla/lista `INSTALLED_APPS`.

### 2. Falta de Rota com `include()` no Projeto
* **Local:** `urls.py` (nível de projeto)
* **Problema:** Ausência do mapeamento principal com a função `include()`, fazendo com que a URL da `home` e todas as rotas secundárias da aplicação ficassem inacessíveis.
* **Correção:** Importado o método `include` e adicionado o `path('', include('portal.urls'))` ao `urlpatterns`.

### 3. Atributo Inexistente no `list_display` do Admin
* **Local:** `admin.py`
* **Problema:** O atributo `especialidade` não existe na superclasse/model `Professor`, mas estava sendo requisitado na configuração de exibição do Django Admin (`list_display`), gerando erro de carregamento no painel.
* **Correção:** Remoção da referência a `especialidade` da lista `list_display`.

### 4. Campos Preenchíveis Ausentes no Formulário
* **Local:** `forms.py` / `models.py`
* **Problema:** Omitiram-se as strings dos atributos preenchíveis `observacao` e `imagem` (na tupla `fields`), impedindo a submissão e o tratamento desses dados via interface.
* **Correção:** Inclusão explícita de `'observacao'` e `'imagem'` na configuração de campos permitidos.

### 5. Falta de Import do `timezone`
* **Local:** `models.py` / `views.py`
* **Problema:** Tentativa de manipulação ou definição de datas/horas padrão sem a presença da biblioteca utilitária do Django, causando `NameError`.
* **Correção:** Adicionada a importação `from django.utils import timezone`.

### 6. Ausência de Parâmetro de Unicidade no Campo  `matricula`
* **Local:** `models.py`
* **Problema:** O campo `matricula` foi declarado sem a restrição de valor único, o que permitiria o cadastro de múltiplos registros com a mesma identificação escolar no banco de dados.
* **Correção:** Adição do parâmetro `unique=True` no campo de texto.

### 7. Redundância de Caminho no `render()`
* **Local:** `views.py`
* **Problema:** Especificação explícita de `template/...` no caminho do arquivo (ex: `render(request, 'template/index.html')`). O Django já busca templates automaticamente dentro do diretório padrão configurado.
* **Correção:** Removido o prefixo redundante, ajustando para `render(request, 'index.html')` (ou `portal/index.html`).

### 8. Referência a Template Inexistente
* **Local:** `views.py`
* **Problema:** O código tentava carregar um arquivo de template que ainda não havia sido criado na árvore do projeto, gerando `TemplateDoesNotExist`.
* **Correção:** Ajustada a view para evitar a quebra, inserindo temporariamente a referência do que a tela deve conter até a entrega do arquivo final.

