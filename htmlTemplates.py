css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://images.unsplash.com/photo-1546776310-eef45dd6d63c?q=80&w=3368&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,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">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
