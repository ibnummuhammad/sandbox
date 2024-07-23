let podNameSpace: string = "kubeflow";
let podName: string = "pipeline-4vqqd-3932826485";
let getCreateTimeSinceEpoch: number = 1721149200000;
let getLastUpdateTimeSinceEpoch: number = 1721408399000;

const date: Date = new Date(getCreateTimeSinceEpoch);
console.log(date);
const hours = date.getHours();
console.log(hours);
const minutes = date.getMinutes();
console.log(minutes);
const day = date.getDate();
console.log(day);
const time = date.getTime();
console.log(time);

const date_kurang = new Date(getCreateTimeSinceEpoch);
date_kurang.setHours(date_kurang.getHours() - 2);
const hours1 = date_kurang.getHours();
console.log(hours1);
const day1 = date_kurang.getDate();
console.log(day1);

console.log("lebih");
const date_lebih = new Date(getCreateTimeSinceEpoch);
date_lebih.setHours(date_lebih.getHours() + 2);
const hours2 = date_lebih.getHours();
console.log(hours2);
const day2 = date_lebih.getDate();
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
