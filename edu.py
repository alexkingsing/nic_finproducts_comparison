intro = '''Esta sección esta orientada a proporcionar información sobre interés compuesto y como funciona, y sobretodo, **porque es tan potente!** 
Esperamos que está sección te inspire a aprender más sobre finanzas personales e inversión, y a crecer tú capital!
\n **Nota**: TODOS los ejemplos y cálculos base se harán con un capital incial de 1,000 USD. Esto es bastante popular en finanzas! 
\n Sin más preámbulo, empecemos!'''

index = ''' 1. ¿Qué es el interés? \U0001F4CD
2. ¿Tipos de interés? \U0001F4CD
3. ¿Interés Simple vs Interés Compuesto? \U0001F4CD'''

interest = ''' La manera más fácil de explicar el interés es: **La ganancia o utilidad que podemos obtener de una inversión.** \n
¿Pero cómo se justifica el interés? ¿De dónde viene? ¿Por qué tengo que darle dinero el banco/prestamista? Sin entrar en una larga historia sobre el origen de los intereses,
esto se pueden explicar como **el retorno (o ganancia) que permite, con cierta seguridad, justificar este riesgo y costo de oportunidad**. \n
Bueno, no es 100% comprensible así, no? Separemos el concepto en partes para entenderlo mejor: \n
1. ***El riesgo***: Esta es la parte más fácil de entender y explicar, aunque **OJO** riesgo puede ser MUCHAS cosas más allá de impago. 
La definición más simple de riesgo es: **Es es la estimación de que tan probable es que la persona/entidad que pide el dinero no lo regrese**. 
Organizaciones grandes como aseguradoras o bancos tienen complejos modelos estadísticos para determinar este número, pero entre personas comunes es, literalmente, al azar.
2. ***El costo de oportunidad***: Este es un poco más complejo y puede dividirse en dos partes:\n 
    * **Inflación**: Esta parte del interés se usa para, de manera simple, **se asegura que el dinero no pierda valor en el tiempo** (un concepto MUY importante en finanzas).
    Este valor suele obtenerse ya sea de la inflación esperada para el país, o de las tasa de interés del Banco Central, o bonos del Tesoro de U.S.A, etc. 
    Asimismo esta cifra suele ser la base de todo el interés: dicho de otra manera, **como mínimo, cualquier préstamo debe pagar el interés asociado a la inflación**.
    Esto con el propósito de que el dinero prestado **no pierda valor en el tiempo**.
    * **Oportunidad**: Esta parte puede considerarse la más compleja y es la que realmente se asocia la 'ganancia' que el prestamista quiere obtener por darte este dinero. 
    Hay muchísimas maneras de calcular esta parte, pero en general esto dependerá de los objetivos de recaudación de la empresa. \n
Matemáticamente el interés puede verse como:'''

###################################### SECTION SEPARATOR #######################################

interest_types_simple = ''' Dependiendo de la conversación que se este teniendo se puede decir que hay varios tipos de interés (tasa fija, variable, etc),
sin embargo para nuestros propósitos discutiremos los dos principales ** Interés simple ** e ** Interés compuesto**. \n 
OJO: Aunque en términos generales estos tipos de interés son estándar, existen diferencias en sus aplicaciones dependiendo del país o institución. **Por favor siempre preguntar y verificar!** \n 
Vamos!! \n
* **Interés simple**: El interés simple es, a como lo dice su nombre, simple! ¿Pero qué quiere decir esto? En pocas palabras, esto quiere decir que **no hay interés sobre interés**
ya sea como deuda o como ganancia, ***no pagas interés sobre el interés de la deuda, ni tampoco obtienes interés sobre las ganancias obtenidas***
el interés simple es una tasa "bruta" que se aplica al principal (en muchos casos diariamente). El interés es a su vez **muy raro** en la vida real, la mayoría del tiempo los préstamos o inversiones funcionan con interés compuesto
¿Pero esto sigue siendo un poco abstracto no? Intentemos con un ejemplo!\n
Antes que todo veamos la fórmula para cálcular el interés:
  '''
interest_types_simple_pt2 = '''
Esto se lee -> El interés es igual al principal "P" por la tasa de interés del período.\n
Ahora si! Vamos al **ejemplo**: Imagina que tomas un préstamo de 10,000 USD para comprar un vehículo a una tasa de interés de 5% anual por 5 años. 
Un cálculo simple nos dice que el interés a pagar por año es de 500 USD anuales, esto es la *ganancia* de quién emite el préstamo. Y listo! \n
Pero que pasa si te retrasas y en vez de pagar exactamente al año? Dependiendo de los términos de tú préstamo podrías estar sujeto a una mora o penalización, pero en cuanto a los interes
**tus intereses a la fecha de pago NO generan más interes** el ÚNICO interés generado es aquel que se origina del principal.
Esta premisa (el interés no genera más interés) es lo que hace que este se llame interés simple. \n
Si quieres verlo gráficamente, **el interés simple es una simple línea recta!**
'''

###################################### SECTION SEPARATOR #######################################

interest_types_compound = '''
* **Interés compuesto**: El interés compuesto, a diferencia del interés simple, SI genera interés sobre interés, y este es su gran poder! (o gran maldición, en algunos casos).
Básicamente funciona de la siguiente manera: 
  1. El interés se aplica cada cierto tiempo (mensual, trimestral, anual, etc) A esto se le llama **periodo de capitalización**, y suele representarse en fracción del año.
  2. Este interés inmediatamente se adiciona al capital principal
  3. Para el próximo periodo, se recalcula el interes de forma (Principal + interés anterior) * tasa de interés = nuevo interés
  4. *Ad infinitum*\n
Al final de esta sección se incluirá un poco más de explicación de la fórmula, pero la forma general del interés compuesto se define matemáticamente así:
'''

interest_types_compound_pt2 = '''
Esto se lee: El valor final(Vf) es igual a, el Principal (P) por **1 más la tasa de interés(r) dividido entre el período de capitalización(n)** elevado **a la tasa de interés dividido entre el período de capitalización**.
Si el periodo de capitalización es anual esto se simplifica a:
'''

interest_types_compound_pt3 =  '''
Pero vamos, para verlo vía fórmulas es fácil encontrar un libro. ¿Qué tal un ejemplo que ilustre la situación? \n
 **Ejemplo**: Tú obtienes un certificado de depósito por valor de 1,000 USD a 1 año con un tasa de interés del 10% (ilustrativa).
 Al final del año, tú recibes 1,000 + 10% = 1,100, pero para los olvidadizos entre nosotros, si se nos va y no retiramos el depósito, el banco automáticamente lo invierte de nuevo!
 pero entonces, ¿qué pasa con nuestro dinero? pues sucede que está renovación es casi como un nuevo certificado, pero ahora el principal no es 1,000, sino 1,100!
 Esto quiero decir que el interés al segundo año sería 1,100 + 10% = 1,210 USD! **O sea, obtuvimos interés sobre nuestro interés!**\n
 Una vez más, como una imagen dice más que mil palabras, veamos una gráfica del interés compuesto. **OJO** presta atención al tipo de curva \U0001F609
'''

###################################### SECTION SEPARATOR #######################################

interest_simvscomp = '''
Una vez definido ambos tipos interés, una buena manera de ver la gran diferencia entre ambos es con una simple comparación: \n
Imagina el siguiente escenario. Tú tienes 1,000 USD que piensas invertir por 10 años y tienes dos opciones de inversión:
1. Un bono que paga 5% de interés al año, por 10 años.
2. Un certificado de depósito que paga 5% de interés al año.
De manera simple ¿Cuál escogerías?
A manera general suenan igual, ¿no? pues no lo son! \n
Los bonos son instrumentos financieros que pagan un **interés simple** es decir, tú retorno **SIEMPRE** es el mismo. Este bono pagaría entonces **50 * 10 = 500 USD en 10 años.** \n
¿Pero y el certificado? Bueno, el certificado con vencimiento anual se renueva cada año, es decir, tus interés del año anterior se suman al principal para formar tú nuevo principal.
Usando la fórmula anteriormente mostrada obtenemos que a 10 años, este certificado de depósito te generaría aprox. **628.90 USD en interés!** \n
Dirás "**Eso solo es una diferencia de 129 USD**, no es mucho para 10 años" y a rasgos generales tendrías razón, pero he aquí la magia del interés compuesto, extendamos esto a 30 años.
Y, cómo un dibujo dice más que mil palabras, veámoslo en una gráfica!
'''

interest_simvscomp_pt2 = '''
¿Ven la diferencia? Misma tasa de interés, mismo período de tiempo, pero el certificado genera el **DOBLE** de intereses que el bono!
Exactamente la diferencia entre ambos es **1,666.86 USD**. \n
Con esto podemos visualizar la clave que le da su poder al interés compuesto **entre más pronto inicies, más grande será tú retorno en el futuro!**. \n
Finalmente una nota: Los productos financieros utilizados acá son para propósitos ilustrativos, al momento de escoger una inversión hay MUCHO más que considerar que solo el retorno
(riesgo, liquidez, ForEx, etc). **Esto no es consejo de inversión**.'''

###################################### SECTION SEPARATOR #######################################

annex = '''
**Esta sección es completamente opcional** y la derivación matemática del interés compuesto: \n
Antes que todo recordemos la fórmula más básica para obtener el interés:
'''

annex_2 = '''
Con esta fórmula podemos calcular el interés que nos generaría una inversión luego de un período. \n
Luego, para encontrar el **total** de dinero que tendríamos al final de ese período tenemos que sumar el principal, o inversión, a los intereses:
'''

annex_3 = '''
Ahora haremos un poco de algebra y lo explicaremos una vez concluido!
'''

annex_4 = '''
Dejamé explicar lo que paso acá: \n
1. Primero substituimos la primera equación (1) en la (2) para tener una forma común de ambas.
2. Luego, usando un poco de álgebra, agrupamos los elementos en común (La P) y obtenemos una nueva equación (3)
Excelente! con esto podemos cálcular cualquier valor final y solo necesitamos saber la tasa de interés del período. Pero, ¿qué pasa si tenemos más de un período? \n
Nuestra equación para más de un período se vería así:
'''

annex_5 = '''
Hay algo que notar acá! Interés para el 2do período (I sub-uno) depende NO del principal, sino del **Valor final del período anterior**. De forma que:
'''

annex_6 = '''
Pero es bastante complicado! Y solo para dos períodos! Una vez más, un poco de algebra nos salva:
'''

annex_7 = '''
Esto es bastante más legible, ¿no? Pero los que están en secundaria notarán que estamos multiplicando dos veces lo mismo. ¿No había algo para simplificar eso? Claro que sí!
'''

annex_8 = '''
Y listo! Si seguimos bien hasta acá notarás que, independientemente de cuantos períodos apliquemos, regresaremos a la misma forma, por lo tanto podemos definir que:
'''

annex_9 = '''
Mucho más bonito, ¿no? y si te fijas bien está **es la misma fórmula** que explicamos en la sección de interés compuesto para el escenario de interés capitalizable anualmente. \n
Faltarían unos pocos pasos para obtener la forma general que toma en cuenta todos los períodos (mensual, trimestral, etc), pero con esto se visualiza claramente la deducción de como llegamos
al interés compuesto desde su definición inicial, hasta la fórmula que cualquier banquero te puede recitar de memoria!
'''