class Publicacao:
    def __init__(self, titulo: str, autor: str, ano_publicacao: int):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibir_info(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao})"


class Livro(Publicacao):
    def __init__(self, titulo: str, autor: str, ano_publicacao: int, isbn: str, genero: str):
        super().__init__(titulo, autor, ano_publicacao)
        self.isbn = isbn
        self.genero = genero 

    def exibir_info(self):
        return f"[LIVRO - {self.genero}] {super().exibir_info()} | ISBN: {self.isbn}"


class Revista(Publicacao):
    def __init__(self, titulo: str, autor: str, ano_publicacao: int, edicao: int, genero: str):
        super().__init__(titulo, autor, ano_publicacao)
        self.edicao = edicao
        self.genero = genero

    def exibir_info(self):
        return f"[REVISTA - {self.genero}] {super().exibir_info()} | Edição: {self.edicao}"


class Podcast(Publicacao):
    def __init__(self, titulo: str, autor: str, ano_publicacao: int, duracao_min: int, genero: str):
        super().__init__(titulo, autor, ano_publicacao)
        self.duracao_min = duracao_min
        self.genero = genero

    def exibir_info(self):
        return f"[PODCAST - {self.genero}] {super().exibir_info()} | Duração: {self.duracao_min} min"


class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.publicacoes = []  

    def adicionar_publicacao(self, pub: Publicacao):
        self.publicacoes.append(pub)

    def remover_publicacao_por_titulo(self, titulo: str):
        for pub in self.publicacoes:
            if pub.titulo.lower() == titulo.lower():
                self.publicacoes.remove(pub)
                print(f"Publicação '{titulo}' removida com sucesso!")
                return
        print(f"Publicação '{titulo}' não encontrada.")

    def listar_publicacoes(self):
        print(f"\nListando publicações da biblioteca '{self.nome}':")
        if not self.publicacoes:
            print("(Nenhuma publicação cadastrada)")
        for pub in self.publicacoes:
            print(" -", pub.exibir_info())

    def buscar_por_autor(self, autor: str):
        encontrados = [pub for pub in self.publicacoes if pub.autor.lower() == autor.lower()]
        print(f"\n Buscando publicações do autor '{autor}':")
        if not encontrados:
            print("Nenhum resultado encontrado.")
        else:
            for pub in encontrados:
                print(" -", pub.exibir_info())


if __name__ == "__main__":
    pub1 = Livro("Galáxias em Guerra", "João Silva", 2020, "978-85-7522-123-4", "Ficção Científica")
    pub2 = Livro("Sombras na Noite", "Maria Souza", 2018, "978-85-1111-222-5", "Policial")
    pub3 = Revista("Futuro Espacial", "Equipe Cosmos", 2021, 58, "Ficção Científica")
    pub4 = Revista("Mistérios Urbanos", "Equipe Investigativa", 2023, 12, "Policial")
    pub5 = Podcast("Crimes que Chocaram o Mundo", "Carlos Dias", 2022, 45, "Crimes Reais")
    pub6 = Podcast("Arquivos Secretos", "Ana Paula", 2021, 30, "Crimes Reais")
    pub7 = Livro("O Último Android", "José Martins", 2024, "978-85-3333-444-6", "Ficção Científica")
    pub8 = Revista("Crimes Reais", "Equipe Verdade", 2020, 101, "Policial")
    pub9 = Podcast("Investigação Sem Fim", "João Silva", 2023, 55, "Crimes Reais")
    pub10 = Livro("Rede de Mentiras", "Carla Menezes", 2019, "978-85-4444-555-7", "Policial")

    biblioteca = Biblioteca("Futuro Digital Leituras")

    for p in [pub1, pub2, pub3, pub4, pub5, pub6, pub7, pub8, pub9, pub10]:
        biblioteca.adicionar_publicacao(p)

    biblioteca.listar_publicacoes()
    biblioteca.remover_publicacao_por_titulo("Mistérios Urbanos")
    biblioteca.listar_publicacoes()
    biblioteca.buscar_por_autor("João Silva")
