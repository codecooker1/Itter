fnm env --use-on-cd | Out-String | Invoke-Expression
cd $(pwd)
npm run dev