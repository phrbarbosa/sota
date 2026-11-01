# Exemplo: uma Revisão `lite` em português

Saída real de `/sota:sota revise lite o plano em plano.md. Sou voluntária da biblioteca. Não me pergunte nada.` no protocolo 1.0.0. O plano foi escrito como teste, e o parecer abaixo está sem edição, inclusive a primeira frase. Custo medido: US$ 1,57 a preços de API, em um modelo da classe Opus, em cerca de 7 minutos. `lite` roda as cinco leituras em um só contexto, então é mais barato e mais fraco que `standard`, como o próprio parecer avisa.

## A entrada: `plano.md`

```markdown
# Mutirão de leitura na biblioteca do bairro

Objetivo: dobrar em um mês o número de crianças que retiram livros.

1. Colocar um cartaz na porta da biblioteca convidando as famílias.
2. Abrir também aos domingos, das 8h às 12h, com dois voluntários.
3. Dar um brinde para cada criança que devolver cinco livros.
4. Não precisamos medir nada: se as crianças vierem, vai dar para ver.
```

## O parecer

Conferência concluída e correções aplicadas. Segue o parecer; `plano.md` não foi alterado.

# Parecer Curia: Mutirão de leitura

**Veredito:** GO WITH CHANGES
**Por quê:** a ideia é barata e reversível, mas como está escrita não alcança crianças novas nem mostra se o objetivo foi atingido.
**Confiança:** média. A conta foi executada e três fontes foram abertas, mas não conheço os números nem as regras da biblioteca.
**Modo:** lite, com as cinco leituras em um só contexto e sem contenção, logo sem independência real. Uma família de modelo.

## Objetivo avaliado
Dobrar em um mês o número de crianças que retiram livros.

**Contestação:** "dobrar em um mês" é hipótese. Não achei taxa de referência para esse tipo de meta, e o esforço depende da base: de 10 para 20 é outra tarefa que de 200 para 400. Mantive o objetivo e a versão curada o trata como hipótese.

## O que precisa mudar
1. **F1. O passo 4 impede saber o resultado** (`verificado`, por leitura).
   - Evidência: a meta é numérica, mas "não precisamos medir nada". Além disso, "se as crianças vierem" conta visita, e a meta é retirada.
   - Correção: contar a base antes e as crianças diferentes toda semana.
2. **F2. O cartaz na porta fala com quem já chegou à porta** (`plausível`).
   - Evidência: em Charlotte, a biblioteca distribuiu fichas nas salas de aula e registrou mais de 14 mil carteirinhas novas em cerca de dois meses. A fonte não traz dados de empréstimo.
   - Correção: ir às escolas e pôr cartazes fora da biblioteca.
3. **F3. O brinde premia outra coisa e fica fora do prazo** (`verificado` na conta; regras reais desconhecidas).
   - O objetivo conta crianças, e o brinde premia volume de livros.
   - Com 1 livro por vez e prazo de 7, 14 ou 21 dias, o máximo em 30 dias é 4, 2 ou 1 devolução. Nesses cenários, ninguém chega a cinco.
   - Correção: dar um marcador de livro na primeira retirada.
4. **F4. O passo 2 supõe autorização e pessoas que uma voluntária pode não controlar** (`plausível`).
   - Evidência: não há responsável nem quem registre os empréstimos, e são 32 a 40 horas de voluntário por mês.
   - Correção: aprovação, escala nomeada e alternativa caso a resposta seja não.

## O que convém mudar
1. **Dar um motivo para vir no domingo** (esforço pequeno): o título promete mutirão de leitura, mas nenhum passo tem leitura. A versão curada inclui contação de histórias, sem prova de que aumente empréstimos: não achei dados sobre isso.
2. **Suspender multa ou bloqueio infantil, se existir** (esforço pequeno): a biblioteca de Yolo relata alta de 28% nos empréstimos em cartões infantis após acabar com as multas. É dado da própria biblioteca, sem grupo de controle e sem período informado.

## O que manter
- **Dois voluntários por domingo:** evita um adulto sozinho com crianças.
- **Meta numérica:** é ela que torna o resultado verificável.
- **Custo baixo e reversível:** dá para testar em poucas semanas.

## Versão curada
**Status:** um contexto novo conferiu o rascunho. F3 e F4 ficaram resolvidos; F1 e F2, parciais. As contas de datas e horas estavam certas. Ele apontou 12 defeitos e 1 perda, e apliquei tudo. **O texto final não foi reconferido.**

```markdown
# Mutirão de leitura na biblioteca do bairro

**Objetivo:** em 28 dias, dobrar o número de crianças diferentes que retiram
livros, em comparação com os 28 dias anteriores à contagem da base.

**Formato:** piloto de 4 domingos. No fim, a coordenação (ou quem responde pela
biblioteca) decide com os números se continua.

## Preparação (sem divulgar nada ainda)
1. **Base e meta.** Contar no registro quantas crianças diferentes retiraram
   livros nos últimos 28 dias, cada uma uma vez, só o total, sem nomes.
   Meta = base × 2. Se o registro não permitir a contagem, combinar um número
   fixo como meta; nesse caso, o resultado não dirá se dobrou.
2. **Aprovação.** Levar este plano à coordenação e confirmar: abertura aos
   domingos, quem abre e fecha, quem registra empréstimos e quem paga os
   marcadores. Sem esse sim, nenhum domingo é anunciado: fazer escolas e cartazes
   no horário atual, com a mesma contagem.
3. **Escala.** Dois nomes por domingo, um suplente e quem conta as histórias.
   Sempre dois adultos presentes. São 32 horas de voluntário só nos domingos,
   fora visitas e contagens.
4. **Regras.** Confirmar o que a criança precisa para ter carteirinha e o prazo de
   empréstimo. Se multa ou bloqueio travar crianças, pedir à coordenação que
   suspenda durante o piloto.
5. **Escolas.** Combinar com uma ou duas escolas próximas uma visita às turmas e o
   envio da ficha de inscrição para casa. Conferir que os 28 dias caem em período
   de aula; se não caírem, adiar o dia 1. Sem escola, seguir só com cartazes
   externos e registrar que a hipótese da escola não foi testada.

## Os 28 dias (dia 1 é uma segunda-feira; domingos nos dias 7, 14, 21 e 28)
6. **Divulgação, dias 1 a 5.** Visita às turmas, ficha para casa. Cartaz na porta
   e em lugares por onde as famílias passam, com datas, horário, "só 4 domingos" e
   o que trazer para fazer a carteirinha.
7. **Domingos, 8h às 12h.** Contação de histórias às 9h, inscrição na hora e
   primeiro empréstimo.
8. **Marcador de livro.** Cada criança ganha um na primeira retirada do período.
   Quantidade = meta, com folga. O brinde por cinco devoluções sai do piloto; a
   devolução segue as regras normais, e o prazo é lembrado em cada empréstimo.
9. **Contagem semanal.** Desde o dia 1, anotar a carteirinha de cada retirada, sem
   nome. Toda segunda: crianças diferentes até agora, crianças em cada domingo,
   fichas devolvidas e carteirinhas novas.
10. **Ponto de virada, dia 15.** Se o acumulado for menor que metade da meta,
    perguntar a cinco famílias o que impede e mudar uma coisa: uma nova escola ou
    o horário do domingo, este com o ok da coordenação e cartazes atualizados.
11. **Fechamento, dia 29.** Levar à coordenação: base, resultado, crianças por
    domingo, horas gastas e custo. A coordenação decide se continua.

## Hipóteses (nada aqui é promessa)
| Hipótese | Como saberemos |
|---|---|
| Dobrar em 28 dias é possível | Contagem do dia 15 e do dia 29 |
| A escola traz crianças novas | Fichas devolvidas e carteirinhas novas |
| Domingo de manhã serve às famílias | Crianças nos dois primeiros domingos |
| O ritmo do dia 15 (metade da meta) indica o final | Comparar dia 15 e dia 29; é suposição |
```

**O que mudou, por achado:**
- **F1:** passos 1, 9, 10 e 11.
- **F2:** passos 5 e 6.
- **F3:** passo 8.
- **F4:** passos 2 e 3.
- **Melhorias:** contação no passo 7, multa no passo 4.

## Divergência em aberto
**Tirar o brinde por cinco devoluções:**
- *A favor de manter:* é a ideia original e o único estímulo à devolução.
- *A favor de tirar:* no estudo de Small e colegas, as recompensas tiveram pouco ou nenhum efeito sobre ler ou não, embora os autores não generalizem (EUA, 6º a 8º ano, 22 entrevistas).
- *Por que segue em aberto:* nenhuma das duas opções foi testada nesta biblioteca. Por isso, o marcador é uma escolha do piloto, não uma prova.

## O que mudaria o veredito
- **Regras que permitam 3 ou mais livros por vez:** derrubam a conta de F3, mas não o desencontro com o objetivo. Teste: ler o regulamento.
- **Coordenação sem verba, chave ou gente para o domingo:** o piloto fica sem o passo 7. Teste: a conversa do passo 2.
- **Primeiros domingos vazios, mesmo com escola:** o mecanismo central falha, e o veredito passa a NOT YET. Teste: contagem do dia 15.

**Pré-mortem:** se falhar em 12 meses, o motivo mais provável é o voluntariado de domingo ter se esgotado sem que os números justificassem mantê-lo.

## Avaliação por dimensão
| Correção | Adequação | Risco | Custo | Execução | Pessoas afetadas | Visão externa |
|---|---|---|---|---|---|---|
| parcialmente correto | parcial | contido | enxuto | adequada | com ressalvas | parcial |

<details><summary>Registro e notas de processo</summary>

| ID | Achado | Classe | Severidade | Status |
|---|---|---|---|---|
| F1 | Medição impossível | único | major | verificado |
| F2 | Cartaz com alcance limitado | único | major | plausível |
| F3 | Brinde desalinhado e fora do prazo | único | major | conta verificada |
| F4 | Autorização e responsáveis ausentes | único | major | plausível |

- **Classes:** "único" é consequência do modo lite, que não tem cadeiras independentes para convergir.
- **Sem perguntas:** como pedido, tratei o que só você sabe como desconhecido, sem preencher por suposição.
- **Fontes que não abriram:** a meta-análise de Deci e colegas e a revisão de Gear e colegas. Não uso nenhuma delas como evidência.
- **Busca em português:** achou relatos de contação e parceria com escolas, sem dados de empréstimo. Vi só os resumos, sem abrir os textos.
</details>

**Fontes abertas:**
- [Charlotte-Mecklenburg: campanha de carteirinhas nas escolas](https://www.naco.org/resources/award-programs/library-card-drive-charlotte-mecklenburg-schools-students-pre-k-through)
- [Yolo County Library: proposta de fim das multas](https://www.webjunction.org/content/dam/WebJunction/Documents/webJunction/2021-06/yolo-presentation-to-board-eliminate-fines.pdf)
- [Small, Arnone e Bennett: recompensas em programas de leitura de férias](https://journals.ala.org/index.php/cal/article/view/6236/8124)
