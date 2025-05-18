# Decriptação de mensagens em imagens dentro de PDF

## Extração das imagens no PDF

**Objetivo:** Aplicar um script que obtenha todos os links do PDF e depois obter aquele que fosse do Google Drive (pois uma das imagens que era o do ovo estava no Google Drive - se não fosse por este script estaria até hoje procurando as imagens  😂 😂 😂).

## Extração de Links em PDFs com PyMuPDF

Este script em Python realiza a extração automática de links contidos em arquivos PDF localizados na mesma pasta onde o script é executado, utilizando a biblioteca PyMuPDF.

### Como funciona

1. **Busca na pasta atual**  
   O script utiliza o diretório atual de execução para listar todos os arquivos PDF presentes, sem a necessidade de informar o caminho manualmente.

2. **Abrir cada PDF**  
   Para cada arquivo PDF encontrado, o script abre o documento usando `fitz.open()`.

3. **Iterar pelas páginas**  
   Em cada página do PDF, o script busca por:
   - **Links:** Utilizando o método `pagina.get_links()`.
   - **Imagens:** Obtidas via `pagina.get_images(full=True)` para tentar verificar se algum link está sobre uma imagem.

4. **Exibição dos links encontrados**  
   Se a página contiver links, o script imprime:
   - A quantidade de links na página
   - A URL (`uri`) de cada link
   - Sua posição aproximada (`bbox`) na página

5. **Verificação de links sobre imagens (opcional)**  
   O código tenta identificar se algum link está localizado sobre uma imagem, embora essa parte possa ser aprimorada.

6. **Fechamento do documento**  
   Após o processamento, o documento é fechado para liberar recursos.

### Código atualizado para buscar PDFs na pasta do script

```python
# Usa o diretório atual do script
pasta_atual = os.getcwd()
encontrar_links_em_pdfs(pasta_atual)
```

### Como Executar  

1. Salve o script como `.py` na pasta dos seus PDFs  
2. Execute com: `python3 find_links_in_pdfs.py`  
   - Varre todos os PDFs, exibindo links com página e posição  
3. Requer instalação: `pip install pymupdf`  

🔍 **Observações**:  

- Detecção de links sobre imagens é básica (pode ser aprimorada)  
- Sugestões: filtro por domínio (ex: Google Drive), seleção de PDF específico ou interface gráfica  

## Comandos para decriptação das imagens

🔍 **Observações**:  

- É necessário ter o Stehide instalado no sistema:

```bash
sudo apt update
sudo apt install steghide
```

## Passo 1: Extrair dados de `chave.jpg`

Execute o comando:

```bash
steghide extract -sf chave.jpg
```

Após isso, será solicitada a **passphrase** (senha):

```bash
Enter passphrase: password
```

> **Dica para a senha:**
>
> * Qual é a senha mais popular e fácil do mundo?
> * 8 caracteres
> * Letras minúsculas
>
> Com base nisso, após uma busca, foi encontrado que provavelmente a senha era `"password"`. 😂

Com a senha correta, a saída será:

```bash
wrote extracted data to 'stegpass.txt'
```

---

## Passo 2: Extrair dados de `ciphertext.jpg`

Repita o processo na imagem `ciphertext.jpg`:

```bash
steghide extract -sf ciphertext.jpg
```

Será gerado o arquivo `enunciado.txt.gpg` que contém dados criptografados:

```bash
wrote extracted data to 'enunciado.txt.gpg'.
```

---

## Passo 3: Extrair dados de `decryptography.jpg`

Também extraia dados da imagem `decryptography.jpg`:

```bash
steghide extract -sf decryptography.jpg
```

Será criado o arquivo `decriptacao.txt` contendo a mensagem:

> "Identifique o algoritmo de decriptação através do padrão de cores nos slides."

---

## Passo 4: Decryptar o arquivo `enunciado.txt.gpg`

Baseando-se no padrão de cores dos slides (o AES estava com uma cor diferente), testamos o algoritmo AES para a decriptação:

```bash
gpg --output enunciado.txt --decrypt enunciado.txt.gpg
```

Será solicitado a senha, que está no arquivo `stegpass.txt`:

```bash
Enter passphrase: 22000311
```

---

## Resultado final

O conteúdo do arquivo `enunciado.txt` era:

> "Envie pelo e-aula a descrição dos passos necessários para realização da atividade."
