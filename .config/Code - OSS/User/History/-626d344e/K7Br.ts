import { Note } from "@prisma/client";

export async function createNote(formData: Note) {
    try {
        const response = await fetch('/api/notes', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        const data = await response
        return data
    } catch
}
