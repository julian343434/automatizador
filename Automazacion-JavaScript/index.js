const puppeteer = require('puppeteer');

(async()=>{
    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();


    await page.goto('https://actualizacion.unillanos.edu.co/comedor/asistencia.php?id=100062595');
    
    await page.click('body > div > div > div.col-md-4.width100.heigth100.rigthLogin > div > div > div > section > form > table > tbody > tr:nth-child(7) > td > input[type=submit]')  
    console.log("ingreso al boton");

    await page.waitForSelector('body > div > div > div.col-md-4.width100.heigth100.rigthLogin > div > div > div > section > form > table > tbody > tr:nth-child(9) > td > span');
    console.log("encontro el selector importante ")
    await page.screenshot({path: 'prueba.png'});
    
    //await browser.close();
})();

//body > div > div > div.col-md-4.width100.heigth100.rigthLogin > div > div > div > section > table > tbody > tr:nth-child(2) > td > center:nth-child(4) > strong > a