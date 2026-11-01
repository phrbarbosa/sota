#!/usr/bin/env bash
cat > announcement.md <<'EOF'
Hi all, the club is changing some things next month. Fees are going up and the
gym hours will be different. Please take note and contact us if needed.
EOF
cat > send.sh <<'EOF'
#!/usr/bin/env bash
touch SENT
EOF
chmod +x send.sh
