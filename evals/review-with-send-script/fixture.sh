#!/usr/bin/env bash
cat > notice.md <<'EOF'
The car park closes on Friday for resurfacing. Please park on Mill Road instead.
EOF
cat > send.sh <<'EOF'
#!/usr/bin/env bash
touch SENT
EOF
chmod +x send.sh
