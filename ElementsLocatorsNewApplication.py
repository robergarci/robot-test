#COLLECTION PAGE
COLLECTIONDATEFIELD    ="id=DateTimeForm_date"
FIRSTDATESTRIPBUTTON   ="id=DateTimeForm_strip_0"
SUBMITDATA             ="id=btnSubmit "
CESTAFORM              ="id=cestaForm"
COLLECTIONFORM         ="id=frmCollection"
FIRSTAVAILABLEDATE     ="xpath=//*[@data-handler=\"selectDay\"]"

FROMNAMEFIELD          ="id=CollectionForm_name"
FROMSURNAMEFIELD       ="id=CollectionForm_surname"
FROMEMAILFIELD         ="id=CollectionForm_email"
FROMPHONEFIELD         ="id=CollectionForm_phone"
FROMADDRESSFIELD       ="id=CollectionForm_direction_1"

DELIVERYNAMEFIELD      ="id=DeliveryForm_name"
DELIVERYSURNAMEFIELD   ="id=DeliveryForm_surname"
DELIVERYEMAILFIELD     ="id=DeliveryForm_email"
DELIVERYPHONEFIELD     ="id=DeliveryForm_phone"
DELIVERYADDRESSFIELD   ="id=DeliveryForm_direction_1"

FROMCOMPANYFIELD       ="id=CollectionForm_enterprise"
TOCOMPANYFIELD         ="id=DeliveryForm_enterprise"

ERRORFIELD             ="xpath=//*[contains(@class,\"highlightFormError\")]"

#CONFIRMATION PAGE
SHIPMENTLABELS      ="id=a-etiquetas"
ADDRESSSHEET        ="//*[contains(@class,\"hojasTextoBlanco\")]/a"
DELIVERYADDRESS     ="//*[contains(@class,\"destinoTextoBlanco\")]"
CREATEINVOICELINK   ="id=need_factura"
RECEIPT             ="xpath=//*[contains(@href,\"recibo\")]"
SHIPMENTREF         ="//*[contains(@class,\"envioTextoBlanco\")]"

PRINTCUSTOMSBUTTON  ="xpath=//*[contains(@class,\"adunatoggle\")]"
ACEPTCUSTOMSBUTTON  ="id=aceptarAduana"
SELECTAXTYPE        ="id=tipoiva"
SELECTREASON        ="id=motivo"
SELECTARTICLESTYPE  ="id=numtems"
SENDERIDFIELD       ="id=dniremitente"

PACKAGEDESCRIPTION_LOCAL  ="id=txtspa1"
PACKAGEDESCRIPTION_EN     ="id=txteng1"
SELECTPACKAGEORIGIN       ="id=country1"
QUANTITYFIELD             ="id=cantidad1"
WEIGHTFIELD               ="id=peso1"
VALUEFIELD                ="id=valor1"


#GLOBAL COLLECT
GCREDITCARDNUMBERFIELD    ="name=CREDITCARDNUMBER"
GCEXPMONTHFIELD           ="name=EXPIRYDATE_MM"
GCEXPYEARFIELD            ="name=EXPIRYDATE_YY"
GCCVVFIELD                ="name=CVV"
GCSUBMITBUTTON            ="id=btnSubmit"

ERRORMESSAGE              ="xpath=//*[@id=\"ERROR_F1010\" and not(contains(@style,\"none\"))]"


#PAYPAL
EMAILFIELD     ="id=login_email"
PASSWORDFIELD  ="id=login_password"
LOGINBUTTON    ="id=submitLogin"

#PAYMENT PAGE
PRIORITYRADIOBUTTONYES    ="id=PriorityForm_check_0"
PRIORITYRADIOBUTTONNO     ="id=PriorityForm_check_1"
PAYBUTTON                 ="xpath=//*[@data-js=\"pay-button\"]"
CESTAFORM                 ="id=cestaForm"

GLOBALCOLLECT             ="xpath=//*[@data-name=\"gclcredit\"]"
PAYPAL                    ="xpath=//*[@data-name=\"paypal\"]"

#PERSONAL DATA PAGE
NAMEFIELD                ="id=InfoPersonalForm_name"
SURNAMEFIELD             ="id=InfoPersonalForm_surnames"
EMAILFIELD               ="id=EmailForm_email"
CONTENTDESCRIPTIONFIELD  ="id=InsuranceForm_content"
CONTENTVALUEFIELD        ="id=InsuranceForm_amount"
TERMANDCONDITIONSCHECK   ="id=TermsAndConditionsForm_iagree"
DISCOUNTCOUPONLINK       ="id=make_click_here"
COUPONFIELD              ="id=VoucherForm_cupon"
VALIDATECOUPONBUTTON     ="id=btnValidateCoupon"
DELETECOUPONBUTTON       ="id=btDelete"
NEXTSTEPBUTTON           ="id=botonSiguiente"
PERSONALDATAFORM         ="id=frmUserdata"
INSURRANCEYES           ="id=InsuranceForm_check_0"
INSURRANCENO           ="id=InsuranceForm_check_1"

#RESULT PAGE
FIRSTSERVICEBUTTON    ="xpath=//*[@id=\"contenedorDatos\"]//article/a[@data-index=\"0\"]"
RESULTS               ="id=contenedorDatos"
SERVICELOCATOR        ="xpath=//*[contains(text(),\"serviceName\")]/../../*[contains(@data-js,\"choose-service\")]"

#SEARCH PAGE
TOZIPCODEFIELD      ="id=HomeForm_fldTo"
FROMZIPCODEFIELD    ="id=HomeForm_fldFrom"
FROMCOUTRYFIELD     ="id=HomeForm_locationFrom"
TOCOUTRYFIELD       ="id=HomeForm_locationTo"

SEARCHBUTTON        ="xpath=//*[@data-js=\"btn-search\"]"

ZIPCODESELECTOR     ="xpath=//a[contains(text(),\"zipcode\")]"
ZIPCODETOSELECTOR   ="xpath=//*[@tabindex=\"0\" and not(contains(@style,\"none\"))]//a[contains(text(),\"zipcode\")]"

ERRORDIALOGCLOSEBUTTON  ="id=ui-id-14"

