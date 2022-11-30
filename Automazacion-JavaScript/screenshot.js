const puppeteer = require('puppeteer');


(async()=>{
    const browser = await puppeteer.launch({headless: false});
    const pageVerificador1= await browser.newPage();
    await pageVerificador1.goto('https://actualizacion.unillanos.edu.co/comedor/reporteindividual.php?id=100062595');
    await pageVerificador1.keyboard.press('End');
    console.log("1");
    function Esperar(){
        console.log("espera 4 segundos");
    }
    setTimeout(Esperar,4000);
    console.log("2");
    await pageVerificador1.screenshot({path: 'prueba.png'});
    console.log("3");

    //const screenshot =setInterval (await pageVerificador1.keyboard.press('End'),2000);
})();