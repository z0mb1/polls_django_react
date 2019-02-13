async function GetQuestions() {
  const resp = await fetch("/api/polls/1/questions/");
  if (resp.status !== 200) {
    console.error("Не удалось получить вопросы");
    return false;
  }
  try {
    return await resp.json();
  } catch {
    alert("can not get questions");
  }
  return false;
}

function GetQuestionsMock() {
  const mock = [
    {
      id: 1,
      items: [
        {
          id: 11,
          value: "м",
          pos: 0,
          question: 1
        },
        {
          id: 12,
          value: "ж",
          pos: 1,
          question: 1
        },
        {
          id: 13,
          value: "веган",
          pos: 2,
          question: 1
        }
      ],
      title: "FAKE Укажите Ваш пол",
      poll: 1
    },
    {
      id: 2,
      items: [
        {
          id: 5,
          value: "<3",
          pos: 0,
          question: 2
        },
        {
          id: 6,
          value: "3-5",
          pos: 1,
          question: 2
        },
        {
          id: 7,
          value: "5-25",
          pos: 2,
          question: 2
        },
        {
          id: 8,
          value: "25-26",
          pos: 3,
          question: 2
        },
        {
          id: 9,
          value: "26-40",
          pos: 4,
          question: 2
        },
        {
          id: 10,
          value: "40+",
          pos: 5,
          question: 2
        }
      ],
      title: "FAKE Укажите Ваш возраст",
      poll: 1
    },
    {
      id: 3,
      items: [
        {
          id: 1,
          value: "клубника",
          pos: 1,
          question: 3
        },
        {
          id: 2,
          value: "ваниль",
          pos: 2,
          question: 3
        },
        {
          id: 3,
          value: "zero",
          pos: 3,
          question: 3
        },
        {
          id: 4,
          value: "вишня",
          pos: 4,
          question: 3
        }
      ],
      title: "FAKE Любимый вкус колы",
      poll: 1
    }
  ];
  return new Promise(resolve => {
    setTimeout(() => resolve(mock), 1000);
  });
}

export { GetQuestionsMock, GetQuestions };
