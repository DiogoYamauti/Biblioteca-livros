const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

mongoose.connect('mongodb://localhost:27017/catalogo_livros', { useNewUrlParser: true, useUnifiedTopology: true });

const livroSchema = new mongoose.Schema({
  titulo: String,
  autor: String,
  isbn: String,
  paginas: Number,
  ano: Number,
  valor: Number
});

const Livro = mongoose.model('Livro', livroSchema);

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
app.set('view engine', 'ejs');

app.get('/', async (req, res) => {
  const { page = 1, limit = 10 } = req.query;
  const currentPage = parseInt(page, 10);
  const limitLivros = parseInt(limit, 10);

  try {
    const livros = await Livro.find()
      .limit(limitLivros)
      .skip((currentPage - 1) * limitLivros)
      .exec();

    const count = await Livro.countDocuments();

    const totalPages = Math.ceil(count / limitLivros);

    const startIndex = (currentPage - 1) * limitLivros + 1;
    const endIndex = Math.min(currentPage * limitLivros, count);

    res.render('index', {
      livros,
      totalPages,
      currentPage,
      startIndex,
      endIndex,
      count,
      limitLivros
    });
  } catch (err) {
    console.error(err);
  }
});

app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
