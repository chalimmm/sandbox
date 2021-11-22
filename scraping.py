from seleniumbase import BaseCase
import re
import html_to_json

class SIAKNG(BaseCase):
    def test_demo_site(self):
        self.open("https://academic.ui.ac.id/main/Authentication/")
        self.type('[name="u"]', self.var1)
        self.type('[name="p"]', self.var2)
        self.click('input[value="Login"]')
        self.assert_title('Selamat Datang - SIAK NG')
        self.open('https://academic.ui.ac.id/main/Schedule/Index')
        self.wait_for_ready_state_complete()
        page_source = str(self.get_page_source())
        
        cuts = []
        
        for m in re.finditer('<table class="box">', page_source):
            cuts.append([m.start(), m.end()])
        
        iter = 0
        for m in re.finditer('</table>', page_source):
            cuts[iter][1] = m.end()
            iter += 1
            if iter >= len(cuts):
                break
        
        filtered_page = ""
        for i in range(len(cuts)):
            filtered_page += page_source[cuts[i][0]:cuts[i][1]]
        
        with open("file_cut.html", "w") as file:
            file.write(filtered_page)
        
        with open("file_cut.html", "r") as file:
            html = file.read()
            json_ = html_to_json.convert_tables(html)
            
            with open("file_cut.json", "w") as jsonFile:
                jsonFile.write(str(json_))
