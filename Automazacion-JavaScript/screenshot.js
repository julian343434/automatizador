const puppeteer = require('puppeteer');


(async()=>{
    const browser = await puppeteer.launch({headless: true});
    const pageVerificador1= await browser.newPage();
    await pageVerificador1.goto('https://actualizacion.unillanos.edu.co/comedor/reporteindividual.php?id=100062595');
    await pageVerificador1.keyboard.press('End');
    const fechas1 =await pageVerificador1.evaluate(()=>{
        const elements= document.querySelectorAll('#excel > table > tbody > tr > td:nth-child(4)');
        const fechas =[];
        for (element of elements) {
            fechas.push(element.innerText);
        }
        return fechas;
    });

    console.log(fechas1[fechas1.length-1]);

    //lee los datos de un json
    
    //
    await pageVerificador1.screenshot({path: 'prueba.png'});

    await browser.close();
    //const screenshot =setInterval (await pageVerificador1.keyboard.press('End'),2000);
})();