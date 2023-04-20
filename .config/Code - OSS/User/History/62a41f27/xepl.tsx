"use client";

import { useState } from "react";

type Props = {
  posts: [Post];
};

type Post = {
  _id: String;
  title: String;
  content: String;
};

export default function Home() {
  return <main></main>;
}
