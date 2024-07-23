let podNameSpace: string = "kubeflow";
let podName: string = "pipeline-4vqqd-3932826485";
let getCreateTimeSinceEpoch: number = 1721149200000;
let getLastUpdateTimeSinceEpoch: number = 1721408399000;

let url: string = "https://grafana.mon.tipnet.xyz/explore";
let datasource: string = "loki-core-staging-79yu";
let expr: string = `{namespace=\\"${podNameSpace}\\",pod=\\"${podName}\\"}|=\`\``;

let panesString: string = `
  {
    "ghd": {
      "datasource": "${datasource}",
      "queries": [
        {
          "refId": "A",
          "expr": "${expr}",
          "queryType": "range",
          "datasource": { "type": "loki", "uid": "${datasource}" },
          "editorMode": "builder"
        }
      ],
      "range": { "from": "${getCreateTimeSinceEpoch}", "to": "${getLastUpdateTimeSinceEpoch}" }
    }
  }
`;
let panesJson: JSON = JSON.parse(panesString);
let panes: string = JSON.stringify(panesJson);
console.log(panes)

const grafanaUrl = new URL(url);
grafanaUrl.searchParams.append("schemaVersion", "1");
grafanaUrl.searchParams.append("panes", panes);
grafanaUrl.searchParams.append("orgId", "1");
console.log(grafanaUrl);
console.log(grafanaUrl.toString());
