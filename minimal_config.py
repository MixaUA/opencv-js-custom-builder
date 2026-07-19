- name: Copy opencv.js to repo root
        run: cp build_out/bin/opencv.js "$GITHUB_WORKSPACE/opencv.js"

      - name: Commit opencv.js to repo
        run: |
          cd "$GITHUB_WORKSPACE"
          git config --global --add safe.directory "$GITHUB_WORKSPACE"
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add opencv.js
          git commit -m "Update opencv.js" || echo "Немає змін"
          git push
