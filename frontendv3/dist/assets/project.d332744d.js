import{l as m,m as o}from"./index.24059398.js";import{r as t}from"./HttpCommon.d6b77f6d.js";const C={thPaddingBorderedSmall:"8px 12px",thPaddingBorderedMedium:"12px 16px",thPaddingBorderedLarge:"16px 24px",thPaddingSmall:"0",thPaddingMedium:"0",thPaddingLarge:"0",tdPaddingBorderedSmall:"8px 12px",tdPaddingBorderedMedium:"12px 16px",tdPaddingBorderedLarge:"16px 24px",tdPaddingSmall:"0 0 8px 0",tdPaddingMedium:"0 0 12px 0",tdPaddingLarge:"0 0 16px 0"},x=c=>{const{tableHeaderColor:e,textColor2:r,textColor1:i,cardColor:n,modalColor:d,popoverColor:p,dividerColor:a,borderRadius:s,fontWeightStrong:l,lineHeight:g,fontSizeSmall:u,fontSizeMedium:j,fontSizeLarge:P}=c;return Object.assign(Object.assign({},C),{lineHeight:g,fontSizeSmall:u,fontSizeMedium:j,fontSizeLarge:P,titleTextColor:i,thColor:o(n,e),thColorModal:o(d,e),thColorPopover:o(p,e),thTextColor:i,thFontWeight:l,tdTextColor:r,tdColor:n,tdColorModal:d,tdColorPopover:p,borderColor:o(n,a),borderColorModal:o(d,a),borderColorPopover:o(p,a),borderRadius:s})},h={name:"Descriptions",common:m,self:x},b=h;class v{createProject(e){return t.post("/api/project/create",e)}getProjects(){return t.get("/api/project/list")}getProject(e){return t.get("/api/project/"+e+"/")}updateProject(e,r){return t.put("/api/project/"+e+"/",r)}syncCode(e){return t.get("/api/project/"+e+"/sync_code")}syncCase(e){return t.get("/api/project/"+e+"/sync_case")}syncResult(e){return t.get("/api/project/"+e+"/sync_result")}syncMerge(e,r){return t.post("/api/project/"+e+"/sync_merge",r)}getSyncLog(){return t.get("/api/project/sync_log")}deleteProject(e){return t.del("/api/project/"+e+"/")}cloneProject(e){return t.get("/api/project/"+e+"/clone")}syncProjectCase(e){return t.get("/api/project/"+e+"/sync")}getProjectTree(e){return t.get("/api/project/"+e+"/files")}getProjectCases(e,r){return t.get("/api/project/"+e+"/cases",{file_name:r})}getProjectSubdirectory(e,r){return t.get("/api/project/"+e+"/subdirectory",{file_name:r})}createEnv(e){return t.post("/api/project/env",e)}getEnv(e){return t.get("/api/project/env/"+e+"/")}getEnvs(){return t.get("/api/project/env/list")}deleteEnv(e){return t.del("/api/project/env/"+e+"/")}updateEnv(e,r){return t.put("/api/project/env/"+e+"/",r)}}const L=new v;export{L as P,b as d,x as s};