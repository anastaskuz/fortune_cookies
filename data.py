import random


PAPERS = ('записка 1', 'записка 2', 'записка дьявола',)

MESSAGES = {
	0: '''
    На столе стоит одна большая миска с печеньем в виде различных фигур. 
    Стол вокруг миски усыпан крошками, а на полу, кажется, валяются смятые в комок бумажки.\n 
    Взять печенье из миски?
    ''',
    1.0: '''
    Осмотрев миску внимательнее, Вы находите ее крайне подозрительной.
    Да и хрустящие под ногами кости, наверное, не просто так тут лежат.\n
    Вы решаете уйти.
    ''',
    1.1: '''
    Осмотрев печенье со всех сторон, Вы не находите в нем ничего подозрительного 
    и решаете откусить __всего один маленький кусочек__...\n
    Под зубами что-то шуршит и мешает насладиться вкусом.\n
    Вы вытаскиваете свернутую бумажку изо рта.\n
    Развернуть?
    ''',
    2.0: '''
    Бумажка явно не съедобная, поэтому Вы комкаете ее в руках и кидаете на 
    стол пока делаете новый укус печенья. Оно оказалось вполне съедобным, даже вкусным.\n
    Забрать всю миску с собой?
    ''',
    2.1: '''
    Кажется, на ней что-то написано.
    Ваши навыки позволяют прочитать все, кроме последней строчки, 
    написанной уже совсем другим, неразборчивым почерком.\n\n
    PAPER\n\n
    Содержимое Вас очень порадовало. Вы сворачиваете бумажку с решаете ее сохранить.\n
    Взять еще одно печенье?
    ''',
    3.0: '''
    "Жадность - не порок, а большое свинство" - возникает у Вас в голове.\n
    Вы покидаете помещение с остатками своего печенья за щеками и крошками на губах.
    ''',
    3.1: '''
    Попытавшись взять новое печенье Вы случайно задеваете рукой миску и сдвигаете ее с места.
    Тут должна быть какая-то забавная смерть.
    ''',
    4.0: '''
    Осознав, что у Вас нет друзей чтобы поделиться этой горой лакомства с ними,
    Вы покидаете помещение с крошками на губах и болью в сердце.
    ''',
    4.1: '''
    Попытавшись поднять миску со стола, Вы понимаете, что что-то идет не так.
    Тут должна быть какая-то забавная смерть.
    ''',
}


def get_paper(papers: tuple = PAPERS):
    return random.choice(papers)
