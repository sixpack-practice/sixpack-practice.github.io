const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8');
const scripts=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
const el=()=>({innerHTML:'',textContent:'',addEventListener(){},classList:{add(){},remove(){}},focus(){},setAttribute(){}});
global.document={querySelector:()=>el(),querySelectorAll:()=>[],addEventListener(){}};
global.window={addEventListener(){},scrollTo(){}};global.location={hash:'#home'};global.localStorage={getItem:()=>null,setItem(){}};
const code=scripts.join('\n').replace('"use strict";','')+`
;module.exports={night:lightsSVG('ram','ahead'),trawl:lightsSVG('trawl','port'),shapes:shapesSVG('ram'),buoyR:buoySVG('pcport'),buoyS:buoySVG('safe'),collision:D.collision(),current:D.current(),compass:D.compass(),tides:D.tides(),lights:D.lights(),hero:heroArt(),logo:'',lessons:LESSONS.length,questions:QUESTIONS.length};`;
const m={exports:{}};new Function('module','require',code)(m,require);
fs.writeFileSync(process.argv[3],JSON.stringify(m.exports));
console.log(Object.entries(m.exports).map(([k,v])=>k+':'+(typeof v==='string'?v.length:v)).join(' '));
