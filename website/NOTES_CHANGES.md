添加了 website 目录：

- website/app.py: Flask 接收端，POST /api/push 会将收到的 JSON 保存到 website/received/ 下。
- website/scan_ai.py: 在本地仓库扫描包含可能 AI 生成标记的文件（关键词匹配），并将结果 POST 到 AI_PUSH_ENDPOINT（默认 http://localhost:8000/api/push）。
- website/hooks/pre-push: pre-push hook wrapper，运行上面的扫描脚本（可复制到 .git/hooks/pre-push 或使用 install-hook.sh 安装）。
- website/install-hook.sh: 将 hooks/pre-push 安装到 .git/hooks。
- website/requirements.txt: 依赖列表（Flask, requests）。

使用步骤（本地）：

1) 启动接收端：
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r website/requirements.txt
   python3 website/app.py

   API 会在 http://0.0.0.0:8000/api/push 接收 POST 请求并保存到 website/received/。

2) 在仓库根目录安装 pre-push hook：
   bash website/install-hook.sh

3) 可选配置：
   - 设置 AI_PUSH_ENDPOINT 环境变量（pre-push 运行时会被 scan_ai.py 使用），例如 export AI_PUSH_ENDPOINT="https://example.com/api/push"。
   - 若希望在发送失败时阻止 git push，设置 AI_HOOK_FAIL_BLOCK=1 环境变量。

注意：客户端的 pre-push hook 在本地运行并将扫描结果发送到 API；服务器端只是保存收到的报告。根据需要可以让服务器在收到后做进一步处理（存储到数据库、触发 CI、通知等）。
