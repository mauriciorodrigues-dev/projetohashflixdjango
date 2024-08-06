from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = list(Filme.objects.all().order_by('-data_criacao'))  # Converte o queryset para lista
    if lista_filmes:  # Verifica se a lista não está vazia
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}

def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:8]  # Use slicing para pegar os primeiros 8
    return {"lista_filmes_em_alta": lista_filmes}

def filme_destaque(request):
    filme = Filme.objects.order_by('-data_criacao').first()  # Use .first() para evitar IndexError
    return {"filme_destaque": filme}
