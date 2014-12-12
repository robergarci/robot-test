#CollectionPageKeywords
ENV                    = "OLD"
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
TOCOMPANYFIELD         ="id=entrega_enterprise"
FROMCOMPANYFIELD       ="id=recogida_enterprise"

#ConfirmationPageKeywords
SHIPMENTLABELS      ="//*[contains(@class,\"etiquetasTextoBlanco\")]/a"
ADDRESSSHEET        ="//*[contains(@class,\"hojasTextoBlanco\")]/a"
DELIVERYADDRESS     ="//*[contains(@class,\"destinoTextoBlanco\")]"
CREATEINVOICELINK   ="id=need_factura"
RECEIPT             ="xpath=//*[contains(@href,\"factura_to_pdf\")]"
SHIPMENTREF         ="//*[contains(@class,\"envioTextoBlanco\")]"

#GlobalCollectKeywords (Not migrated yet)

#PayPalKeywords (Not migrated yet)

#PaymentPageKeywords
PRIORITYRADIOBUTTONYES  ="id=check_recomendacion_yes"
PRIORITYRADIOBUTTONNO   ="id=check_recomendacion_no"
PAYBUTTON               ="id=realizarpago"     
CESTAFORM               ="xpath=//*[contains(@class,\"metodoPago\")][1]"
PAYMENTERROR            =""
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
INSURRANCEYES           ="id=check_coberture"
INSURRANCENO            ="id=check_coberture_no"
PERSONALDATAERROR       ="//*[contains(@class,\"highlightFormError\")]"

#ResultsPageKeywords
FIRSTSERVICEBUTTON      ="xpath=//div[@class=\"elegirServicio\"][1]"
RESULTS                 ="id=contenedorDatos"


SERVICELOCATOR          ="xpath=//*[contains(@value,\"serviceName\")]//..//*[@class=\"elegirServicio\"]"

#SearchKeywords
TOZIPCODEFIELD          ="id=cp_hasta"
FROMZIPCODEFIELD        ="id=cp_desde"
SEARCHBUTTON            ="xpath=//div[@class=\"button_search\"]"

ZIPCODESELECTOR         ="xpath=//a[contains(.,\"zipcode\")]"
ZIPCODETOSELECTOR       ="xpath=//*[@tabindex=\"0\" and not(contains(@style,\"none\"))]//a[contains(.,\"zipcode\")]"

ERRORDIALOGCLOSEBUTTON  ="xpath=//*[@class=\"jqiclose\"]"
FROMCOUTRYFIELD         ="id=ol5_select"
TOCOUTRYFIELD           ="id=dl5_select"