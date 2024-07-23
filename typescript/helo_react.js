var podNameSpace = "kubeflow";
var podName = "pipeline-4vqqd-3932826485";
var getCreateTimeSinceEpoch = 1721149200000;
var getLastUpdateTimeSinceEpoch = 1721408399000;
var date = new Date(getCreateTimeSinceEpoch);
console.log(date);
var hours = date.getHours();
console.log(hours);
var minutes = date.getMinutes();
console.log(minutes);
var day = date.getDate();
console.log(day);
var time = date.getTime();
console.log(time);
var date_kurang = new Date(getCreateTimeSinceEpoch);
date_kurang.setHours(date_kurang.getHours() - 2);
var hours1 = date_kurang.getHours();
console.log(hours1);
var day1 = date_kurang.getDate();
console.log(day1);
console.log("lebih");
var date_lebih = new Date(getCreateTimeSinceEpoch);
date_lebih.setHours(date_lebih.getHours() + 2);
var hours2 = date_lebih.getHours();
console.log(hours2);
var day2 = date_lebih.getDate();
console.log(day2);
// let url: string = "https://grafana.mon.tipnet.xyz/explore";
// let datasource: string = "loki-core-staging-79yu";
// let expr: string = `{namespace=\\"${podNameSpace}\\",pod=\\"${podName}\\"}|=\`\``;
// let panesString: string = `
//   {
//     "ghd": {
//       "datasource": "${datasource}",
//       "queries": [
//         {
//           "refId": "A",
//           "expr": "${expr}",
//           "queryType": "range",
//           "datasource": { "type": "loki", "uid": "${datasource}" },
//           "editorMode": "builder"
//         }
//       ],
//       "range": { "from": "${getCreateTimeSinceEpoch}", "to": "${getLastUpdateTimeSinceEpoch}" }
//     }
//   }
// `;
// let panesJson: JSON = JSON.parse(panesString);
// let panes: string = JSON.stringify(panesJson);
// console.log(panes)
// const grafanaUrl = new URL(url);
// grafanaUrl.searchParams.append("schemaVersion", "1");
// grafanaUrl.searchParams.append("panes", panes);
// grafanaUrl.searchParams.append("orgId", "1");
// console.log(grafanaUrl);
// console.log(grafanaUrl.toString());
