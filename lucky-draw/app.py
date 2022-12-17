from js import document, localStorage
from luckydraw import LuckyDraw

class Store:
    
    def __init__(self):
        self.lucky = None
        self.total_draw = 0

        self.hidden = False

    def updateParticipants(self, p):
        self.total_draw = 0
        self.lucky = LuckyDraw(p)

    def nextParticipant(self):
        self.total_draw += 1
        return self.lucky.drawNext() if self.lucky else ""

    def hideTextArea(self):
        if self.hidden:
            return

        if not self.fill_page:
            return

        self.fill_page.hide()
        self.hidden = True

class FillPage:

    def __init__(self, store):
        self.store = store
        self.store.fill_page = self

        self.participants_textarea = Element("participants")
        if p := localStorage.getItem("participants"):
            self.participants_textarea.write(p)
            self.restoreParticipants(p)

    def updateParticipants(self):
        self.store.updateParticipants(self.participants_textarea.value.split("\n"))

    def click(self):
        localStorage.participants = self.participants_textarea.value
        self.updateParticipants()

    def restoreParticipants(self, participants):
        self.participants_textarea.write(localStorage.participants)
        self.updateParticipants()

    def hide(self):
        page = Element("fill-page")
        page.element.setAttribute("hidden", "")

class DrawPage:

    def __init__(self, store):
        self.store = store

        self.result_list = Element("result-list")
        self.result_template = Element("result-template")
        self.result_template_li = Element("result-template").select("li", from_content=True)

        self.count = 0

    def click(self):
        self.store.hideTextArea()
        new_result = self.result_template_li.clone(self.count, self.result_template)
        new_result.write(self.store.nextParticipant())
        self.count+=1

if __name__ == "__main__":
    s = Store()
    fp = FillPage(s)
    dp = DrawPage(s)
