import fitz  # PyMuPDF
import os

def encontrar_links_em_pdfs(pasta_pdf):
    for arquivo in os.listdir(pasta_pdf):
        if arquivo.endswith(".pdf"):
            caminho_pdf = os.path.join(pasta_pdf, arquivo)
            doc = fitz.open(caminho_pdf)
            print(f"🔍 Verificando: {arquivo}")

            for pagina_num, pagina in enumerate(doc):
                links = pagina.get_links()
                imagens = pagina.get_images(full=True)

                if not links:
                    continue

                print(f"Página {pagina_num + 1} tem {len(links)} links.")

                for link in links:
                    tipo = link.get("kind")
                    uri = link.get("uri")
                    bbox = link.get("from")
                    
                    if uri:
                        print(f"➡️ Link encontrado: {uri} na posição {bbox}")

                    # Verificar se o link está sobre alguma imagem
                    for imagem in imagens:
                        xref = imagem[0]
                        img_bbox = doc.extract_image(xref)['bbox'] if 'bbox' in doc.extract_image(xref) else None

            doc.close()

# Usa o diretório atual do script
pasta_atual = os.getcwd()
encontrar_links_em_pdfs(pasta_atual)
