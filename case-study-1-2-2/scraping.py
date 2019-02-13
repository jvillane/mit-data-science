from goose import Goose

# how to get links
# load https://www.publimetro.cl/cl/mundo/
# execute in the browser console:
#   var links = $(".tit > a");
#   var array = [];
#   for(i=0; i<links.length; i++){ array.push(links[i].href); };
#   array;

articles = [
    'https://www.publimetro.cl/cl/noticias/2019/02/13/chapo-muro-texas.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/roban-bonsais-facebook.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/cambio-climatico-mundo.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/vaticano-cuatro-cinco-sacerdotes-homosexuales.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/extrano-leopardo-negro-primera-fotografia-100-anos-kenia-will-burrad-lucas.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/filtran-carta-del-papa-maduro.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/delcy-rodriguez-vicepresidenta-venezuela-ayuda-humanitaria-contaminada-cancerigena.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/carcel-todas-las-carceles-condena-chapo-guzman.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/ayuda-humanitaria-venezuela-2.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/declaran-culpable-al-chapo-cadena-perpetua-la-gravedad-crimenes.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/haiti-3.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/argentina-mato-esposa.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/cadena-humanitaria-venezuela-guaido.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/que-hay-detras-del-plan-de-hungria-para-que-las-mujeres-tengan-mas-de-cuatro-hijos.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/congo-vacuna-ebola.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/canada-mexicanos-exclavizados.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/claves-historico-juicio-independentistas-catalanes-espana.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/asi-es-ultima-thule-el-muneco-de-nieve-espacial-nasa-ultima-thule-mundo-mas-lejano-visto-por-humanidad.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/11/contraloria-venezolana-dinero-guaido.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/11/meghan-markle-carta-padre.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/11/humanos-contaminacion-mar-surfista-video-viral.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/11/osos-polares-rusia.html',
    'https://www.publimetro.cl/cl/social/2019/02/11/insectos-mundo-extincion-colapso-catastrofico-ecosistemas-naturaleza-viral.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/papa-menor-grabado-iniciando-incendio-coronel-culpa-los-amigos-lo-estan-cargando.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/coronel-libertad-coronel-menores-supervision.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/chadwick-ulloa-biobio-no-me-digas-lo-que-tengo-que-hacer.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/alerta-piromana-97-personas-condenadas-incendiar-bosques-los-ultimos-cinco-anos.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/barrio-meiggs-avenida-bascunan-guerrero-estara-cerrada-al-menos-dos-dias-tras-incendio.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/adolescente-autor-incendio-coronel-redes-sociales-video-funa.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/sur-al-limite-calor-incandescente-los-sospechosos-siempre.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/rellenos-sanitario.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/13/ropa-reparar-huella-carbono.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/tres-trabajadores-empresa-telefonica-detenidos-causar-incendio-nuble.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/calzados-beba-remata-stock-500-del-cierre-total.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/pinera-venezuela-dictadura-maduro.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/chicureo-puma-rescate-zoologico.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/magallanes-intendenta-gobernador-renuncia-pinera.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/coronel-incendio-menor-capturado.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/catrillanca-disparo-fach-peritaje-balistico.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/toque-de-queda-concepcion-descarta-huber.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/barrio-meiggs-incendio-ciego-bomberos-heridos.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/evopoli-lanza-elige-incluir-campana-busca-incentivar-la-tolerancia-la-diversidad.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/coronel-incendio-menores-intencional.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/nicolas-soto-murio-bombero-golpeado-balde-helicoptero-combatiendo-incendios-la-araucania.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/permiso-circulacion-multas-transito-no-asi-ponte-las-pilas-no-podras-renovar-permiso-circulacion.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/parricidio-menor-puente-alto-margarita-margarita-jerez.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/metrotren-nos-aprueba-con-un-63-segun-la-encuesta-de-satisfaccion-de-usuarios.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/incendios-sur-decretan-toque-queda-la-provincia-concepcion-evitar-incendios-intencionales.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/incendio-galeria-comercial-barrio-meiggs.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/falta-uno-dos-primer-ten-tanker-volvio-estar-operativo-segundo-cumplira-papeleo-despegar-al-mediodia.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/impresionante-avance-llamas-incendios-bio-bio-penco-villa-italia.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/investigan-intencionalidad-incendios-forestales-simultaneos-biobio-villa-italia-penco.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/intento-robo-cajero-automatico-provoca-explosion-sucursal-bancaria.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/incendios-forestales-region-biobio-simultaneos-evacuacion-peligro-viviendas.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/gobierno-migracion.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/migracion-gobierno-espacio-publico-bellolio.html',
    'https://www.publimetro.cl/cl/noticias/2019/02/12/estas-fueron-las-frases-mas-potentes-de-el-negro-palma-salamanca-a-the-clinic.html',
    'https://www.publimetro.cl/cl/noticias/2017/08/29/les-apagaron-el-negocio-aduanas-lleva-mas-de-75-millones-de-cajetillas-de-cigarrillos-incautadas-este-ano.html',
    'https://www.publimetro.cl/cl/publimetro-tv/2017/08/29/salah-tras-fallo-del-tas-ahora-tenemos-dedicarnos-clasificar.html',
    'https://www.publimetro.cl/cl/noticias/2017/08/29/duro-round-aborto-bachelet-responde-pinera-no-puede-cambiar-decision-la-mayoria.html',
    'https://www.publimetro.cl/cl/publimetro-tv/2017/08/29/salah-tras-fallo-del-tas-ahora-tenemos-dedicarnos-clasificar.html',
    'https://www.publimetro.cl/cl/grafico-chile/2017/08/29/u-humillacion-colo-colo.html',
    'https://www.publimetro.cl/cl/destacado-tv/2017/08/29/terrorifico-cocodrilos-ingresan-al-patio-trasero-una-casa-texas.html',
]
g = Goose()

for num, article in enumerate(articles, start=1):
    print("Article {}: {}".format(num, article))
    article = g.extract(url=article)

    with open('files/title-' + str(num) + '.txt', 'w+') as titleFile:
        titleFile.write(article.title.encode('utf-8').strip())
    with open('files/article-' + str(num) + '.txt', 'w+') as contentFile:
        contentFile.write(article.cleaned_text.replace('\n', ""))

print '-- The end'
