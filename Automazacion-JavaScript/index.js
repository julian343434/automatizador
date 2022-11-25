const puppeteer = require('puppeteer');


(async()=>{
    
    //valores por default
    puede_consultar ='body > div > div > div.col-md-4.width100.heigth100.rigthLogin > div > div > div > section > table > tbody > tr:nth-child(2) > td > center:nth-child(4) > strong > a';
    no_hay_cupos='body > div > div > div.col-md-4.width100.heigth100.rigthLogin > div > div > div > section > form > table > tbody > tr:nth-child(9) > td > span'
    registrar='body > div > div > div.col-md-4.width100.heigth100.rigthLogin > div > div > div > section > form > table > tbody > tr:nth-child(7) > td > input[type=submit]'
    //ABRE LOS NAVEGADORES
    
    //deivid
    const browser = await puppeteer.launch({headless: true});
    const page = await browser.newPage();
    link1=false;
    //daikiry
    const browser2 = await puppeteer.launch({headless: true});
    const page2 = await browser2.newPage();
    link2=false;

    await page2.goto('https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062585');
    await page.goto('https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062595');

    while (true){
        try{
            //BOTON REGISTRAR
            //deivid
            consulta=await page.$(no_hay_cupos);
            if (consulta ==null){    
                await page.click(registrar)  
                console.log("ingreso al boton1");
            }else{
                link1=true;
            }    
        }catch(e){
            console.log("fallo al registrar usuario 1");
            await page.reload();
        }
        
        
        try{
            //BOTON REGISTRAR
            //daikiry
            if (consulta==null){
                consulta=await page2.$(no_hay_cupos);
                await page2.click(registrar)  
                console.log("ingreso al boton2");    
            }else{
                link2=true;
            }
        }catch(e){
            console.log("fallo al registrar usuario 2");
            await page2.reload();
        }    
        

        if (link1 && link2 == true){
            console.log("exitoso para los dos usuarios");
            break;
        }
}

    


    // no hay cupo disponible
    //await page.waitForSelector('body > div > div > div.col-md-4.width100.heigth100.rigthLogin > div > div > div > section > form > table > tbody > tr:nth-child(9) > td > span');
    //console.log("encontro el selector importante ")

    //Consulte si se registro o no
    //await page.waitForSelector('body > div > div > div.col-md-4.width100.heigth100.rigthLogin > div > div > div > section > form > table > tbody > tr:nth-child(9) > td > center > strong > a');
    //await page.screenshot({path: 'prueba.png'});
    
    await browser.close();
    await browser2.close();
})();

//body > div > div > div.col-md-4.width100.heigth100.rigthLogin > div > div > div > section > table > tbody > tr:nth-child(2) > td > center:nth-child(4) > strong > a