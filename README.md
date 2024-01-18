# ProjektuDarbs
Automatizēt Nvidia tīmekļa lapas atvēršanu, pāreju uz draivera informācijas lapu un draivera versijas parādīšanu konsoles ekrānā.

# Problema 
Katru dienu spēlētāju pasaulē aktuāla problēma ir nepieciešamība sekot līdzi pašreizējām draivera versijām savā personālajā datorā, lai panāktu optimālu grafikas kartes veiktspēju. Tādas programmas kā GeForce Experience atvēršana, lai pārbaudītu instalētos draiverus, kļūst laikietilpīgs process, jo tā nodrošina plašu funkcionalitāti, ne tikai informāciju par draiveriem. Jaunais skripts atrisina šo aktuālo problēmu, sniedzot pašreizējās draivera versijas pārbaudes rezultātus tikai 9 sekunžu laikā (manā gadījumā). Tas ievērojami vienkāršo un paātrina optimālas videokartes veiktspējas nodrošināšanas procesu spēlētājiem un citiem lietotājiem.

# Bibliotekas 
selenium: Šī bibliotēka nodrošina rīkus tīmekļa pārlūkprogrammas automatizēšanai. Šajā kontekstā tā tiek izmantota programmatiskai mijiedarbībai ar tīmekļa lapu un informācijas iegūšanai.

webdriver: Šī ir selenium daļa, kas nodrošina saskarni mijiedarbībai ar dažādām pārlūkprogrammām. Šajā gadījumā kods ir vērsts uz darbu ar pārlūku Chrome.

# Īss koda apraksts
webdriver.Chrome(service=service, options=option): Tiek izveidots Chrome tīmekļa draivera gadījums, izmantojot opcijas un pakalpojumu.
  
driver.get('https://www.nvidia.com/Download/index.aspx'): Pārlūkprogramma pāriet uz norādīto Nvidia tīmekļa vietni.

driver.find_element(By.XPATH, "//btn_drvr_lnk_txt"): Šajā rindā, izmantojot XPath, tiek atrasts tīmekļa lapas elements un tas tiek piešķirts mainīgajam login_form.

login_form.click(): Uz atrastā elementa tiek veikts klikšķis, kas, domājams, ir poga, lai dotos uz draivera informācijas lapu.

driver.find_element(By.ID, "tdVersion"): Tiek meklēts elements ar ID "tdVersion", kas, iespējams, satur informāciju par draivera versiju.

print(driver.vers.text): Uz konsoles izdrukā atrastā elementa (draivera versija) teksta saturu.
