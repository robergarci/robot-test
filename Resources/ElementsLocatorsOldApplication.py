#CollectionPageKeywords
COLLECTIONDATEFIELD    ="id=fecha_recogida"
FIRSTDATESTRIPBUTTON   ="id=btnHorario1"
SUBMITDATA 			   ="xpath=//div[@class=\"botonSiguiente\"]"
COLLECTIONFORM         ="id=frmAddressData"
FIRSTAVAILABLEDATE     ="xpath=//*[contains(@class,\"good_date\")][1]"

FROMNAMEFIELD          ="id=recogida_name"
FROMSURNAMEFIELD       ="id=recogida_surname"
FROMEMAILFIELD         ="id=recogida_email"
FROMPHONEFIELD         ="id=recogida_tfno"
FROMADDRESSFIELD       ="id=recogida_address"

DELIVERYNAMEFIELD      ="id=entrega_name"
DELIVERYSURNAMEFIELD   ="id=entrega_surname"
DELIVERYEMAILFIELD     ="id=entrega_email"
DELIVERYPHONEFIELD     ="id=entrega_tfno"
DELIVERYADDRESSFIELD   ="id=entrega_address"

ERRORFIELD             ="xpath=//*[contains(@style,\"background-color: rgb(255, 153, 153)\")]"

#ConfirmationPageKeywords (Not migrated yet)

#GlobalCollectKeywords (Not migrated yet)

#PayPalKeywords (Not migrated yet)

#PaymentPageKeywords
PRIORITYRADIOBUTTONYES  ="id=check_recomendacion_yes"
PRIORITYRADIOBUTTONNO   ="id=check_recomendacion_no"
PAYBUTTON               ="id=realizarpago"     
CESTAFORM               ="xpath=//*[contains(@class,\"metodoPago\")][1]"

GLOBALCOLLECT           ="id=checkbanesto"
PAYPAL                  ="id=checkpaypal"

#PersonalDataPageKeywords
NAMEFIELD               ="id=p_name"
SURNAMEFIELD            ="id=p_surname"
EMAILFIELD              ="id=p_email"
CONTENTDESCRIPTIONFIELD ="id=p_envoi_content"
CONTENTVALUEFIELD       ="id=p_content_value"
TERMANDCONDITIONSCHECK  ="id=p_forbidden"
DISCOUNTCOUPONLINK      ="id=make_click_here"
COUPONFIELD             ="id=p_discount_coupon"
VALIDATECOUPONBUTTON    ="xpath=//input[@id=\"btnValidateCoupon\"]/preceding-siblings::div[@class=\"btnTest botonTextoInterior botonTest\"]"
DELETECOUPONBUTTON      ="xpath=//input[@id=\"btnValidateCoupon\"]/following-siblings::div[@class=\"btDelete\"]"
NEXTSTEPBUTTON          ="xpath=//div[@class=\"botonSiguiente\"]"
PERSONALDATAFORM        ="id=frmUserdata"

#ResultsPageKeywords
FIRSTSERVICEBUTTON      ="xpath=//div[@class=\"elegirServicio\"][1]"
RESULTS                 ="id=contenedorDatos"
PERSONALDATAPAGE        ="https://francia:corcega@pre.packlink.es/datos-personales"

SERVICELOCATOR          ="xpath=//*[contains(text(),\"serviceName\")]/../../*[contains(@data-js,\"choose-service\")] #Not migrated"

#SearchKeywords
TOZIPCODEFIELD          ="id=cp_desde"
FROMZIPCODEFIELD        ="id=cp_hasta"
SEARCHBUTTON            ="xpath=//div[@class=\"button_search\"]"

ZIPCODESELECTOR         ="xpath=//a[contains(.,\"zipcode\")]"
ZIPCODETOSELECTOR       ="xpath=//*[@tabindex=\"0\" and not(contains(@style,\"none\"))]//a[contains(.,\"zipcode\")]"

ERRORDIALOGCLOSEBUTTON  ="xpath=//*[@class=\"jqiclose\"]"