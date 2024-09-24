from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

@app.route('/')
def home():
    return render_template("")