async function send(text: string) {
  const trimmed = text.trim()
  if (!trimmed) return

  const now = new Date().toLocaleTimeString()

  setMessages((prev) => [
    ...prev,
    { id: crypto.randomUUID(), role: 'user', content: trimmed, time: now },
  ])

  setInput("")
  setIsTyping(true)

  const res = await fetch("http://127.0.0.1:8000/chat/stream", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: "default",
      message: trimmed,
    }),
  })

  const reader = res.body?.getReader()
  const decoder = new TextDecoder()

  let assistantText = ""

  setMessages((prev) => [
    ...prev,
    {
      id: crypto.randomUUID(),
      role: "assistant",
      content: "",
      time: new Date().toLocaleTimeString(),
    },
  ])

  while (true) {
    const { value, done } = await reader!.read()
    if (done) break

    const chunk = decoder.decode(value)
    assistantText += chunk
    setMessages((prev) => {
      const copy = [...prev]
      const last = copy[copy.length - 1]
      last.content = assistantText
      return copy
    })
  }

  setIsTyping(false)
}