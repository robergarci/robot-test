ENV                    = "KOKUDO"

#-------------------COLLECTION PAGE---------------------#
COLLECTIONDATEFIELD    ="id=fecha_recogida"
FIRSTDATESTRIPBUTTON   ="id=DateTimeForm_strip_0"
SUBMITDATA             ="id=btnSubmit"
CESTAFORM              ="xpath=//*[@class=\"datos_pedido\"]"
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
ERRORFIELD             ="//*[@class=\"highlightFormError error\"]"
BUTTONCOPYDATA         ="id=chkCopyData"

#---------------------CONFIRMATION PAGE--------------------------------#
SHIPMENTLABELS      ="id=a-etiquetas"
ADDRESSSHEET        ="//*[contains(@class,\"hojasTextoBlanco\")]/a"
DELIVERYADDRESS     ="//*[contains(@class,\"destinoTextoBlanco\")]"
CREATEINVOICELINK   ="id=need_factura"
RECEIPT             ="xpath=//*[contains(@href,\"recibo\")]"
SHIPMENTREF         ="xpath=//*[contains(@class,\"envioTextoBlanco\")]"

PRINTCUSTOMSBUTTON  ="xpath=//*[contains(@class,\"adunatoggle\")]"
ACEPTCUSTOMSBUTTON  ="id=aceptarAduana"
SELECTAXTYPE        ="id=tipoiva"
SELECTREASON        ="id=motivo"
SELECTARTICLESTYPE  ="id=numtems"
SENDERIDFIELD       ="id=dniremitente"

PACKAGEDESCRIPTION_LOCAL  ="id=LineaFacturaAduanaForm_0_txtspa"
PACKAGEDESCRIPTION_EN     ="id=LineaFacturaAduanaForm_0_txteng"
SELECTPACKAGEORIGIN       ="id=LineaFacturaAduanaForm_0_country"
QUANTITYFIELD             ="id=LineaFacturaAduanaForm_0_cantidad"
WEIGHTFIELD               ="id=LineaFacturaAduanaForm_0_peso"
VALUEFIELD                ="id=LineaFacturaAduanaForm_0_valor"


#----------------------GLOBAL COLLECT-----------------------#
GCREDITCARDNUMBERFIELD    ="name=CREDITCARDNUMBER"
GCEXPMONTHFIELD           ="name=EXPIRYDATE_MM"
GCEXPYEARFIELD            ="name=EXPIRYDATE_YY"
GCCVVFIELD                ="name=CVV"
GCSUBMITBUTTON            ="id=btnSubmit"

ERRORMESSAGE              ="xpath=//*[@id=\"ERROR_F1010\" and not(contains(@style,\"none\"))]"


#---------------------PAYPAL----------------------------------#
EMAILFIELD     ="id=login_email"
PASSWORDFIELD  ="id=login_password"
LOGINBUTTON    ="id=submitLogin"

#-----------------------PAYMENT PAGE----------------#
PRIORITYRADIOBUTTONYES    ="id=PriorityForm_check_0"
PRIORITYRADIOBUTTONNO     ="id=PriorityForm_check_1"
PAYBUTTON                 ="id=realizarpago"     
PAYMENTERROR              ="xpath=//*[@class=\"botonSiguiente disabled\"]"

GLOBALCOLLECT             ="xpath=//*[@data-name=\"gclcredit\"]"
PAYPAL                    ="xpath=//*[@data-name=\"paypal\"]"

#-----------------PERSONAL DATA PAGE--------------------------#
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
PERSONALDATAFORM         ="xpath=//div[@class=\"contenidoPersonal\"]"
INSURRANCEYES            ="id=InsuranceForm_check_0"
INSURRANCENO             ="id=InsuranceForm_check_1"
PERSONALDATAERROR        ="//*[contains(@class,\"highlightFormError\")]"

#----------------------RESULT PAGE--------------------------------#
FIRSTSERVICEBUTTON      ="xpath=//*[@class=\"elegirServicio\"]"
RESULTS                 ="xpath=//*[@class=\"elegirServicio\"]"
PERSONALDATAPAGE        ="https://francia:corcega@pre.packlink.es/datos-personales"
SERVICELOCATOR          ="xpath=//*[@class=\"service_name\"]//p//text()[contains(.,\"serviceName\")]/../../../..//*[@class=\"elegirServicio\"]"

#-----------------------SEARCH PAGE--------------------------------------#
TOZIPCODEFIELD      ="id=HomeForm_fldTo"
FROMZIPCODEFIELD    ="id=HomeForm_fldFrom"
FROMCOUTRYFIELD     ="id=HomeForm_locationFrom"
TOCOUTRYFIELD       ="id=HomeForm_locationTo"
SEARCHBUTTON        ="id=btnSearch"
ZIPCODESELECTOR     ="xpath=//*[contains(text(),\"zipcode\")]"
ZIPCODETOSELECTOR   ="xpath=//*[@tabindex=\"0\" and not(contains(@style,\"none\"))]//*[contains(text(),\"zipcode\")]"
ERRORDIALOGCLOSEBUTTON  ="xpath=//*[@class=\"jqiclose\"]"
ADDPARCELBUTTON     ="id=mas1"
COPYLASTPACKAGE     ="id=copyLastPacket_link"

#----------------------LOGIN--------------------------------------------#
LOGINPASSWORDFIELD = "xpath=//input[@id=\"LoginForm_password\"]"
LOGINEMAILFIELD = "xpath=//input[@id=\"loginEmail\"]"
USERLOGINBUTTON = "id=requestLogin"
USERLOGOUTBUTTON = "xpath=//a[contains(@href,\"logout\")]"
USERLOGINERRORMESSAGE =  "xpath=//*[@id=\"user-form\"]/*[contains(@class,\"errorMessage\")]"
SHOWLOGINBUTTON  = "id=headerLogin"
USERLOGINFORM  =  "id=user-form"