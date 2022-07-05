using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Controllers
{
    public class SpecieController : Controller
    {
        private readonly ISpecieRepository _specieRepository;

        public SpecieController(ISpecieRepository specieRepository) =>
            _specieRepository = specieRepository;

        // GET: Specie
        public async Task<IActionResult> Index() =>
            View(await _specieRepository.GetAll());

        // GET: Specie/Details/5
        public async Task<IActionResult> Details(int id)
        {
            if (await _specieRepository.GetById(id) is Specie specie)
                return View(specie);

            return NotFound();
        }

        // GET: Specie/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Specie/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name")] Specie specie)
        {
            if (ModelState.IsValid)
            {
                await _specieRepository.Add(specie);
                return RedirectToAction(nameof(Index));
            }
            return View(specie);
        }

        // GET: Specie/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            if (await _specieRepository.GetById(id) is Specie specie)
                return View(specie);

            return NotFound();
        }

        // POST: Specie/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name")] Specie specie)
        {
            if (id != specie.Id)
                return NotFound();


            if (ModelState.IsValid)
            {
                try
                {
                    await _specieRepository.Update(specie);
                }
                catch (DbUpdateConcurrencyException)
                {
                    throw;
                }
                return RedirectToAction(nameof(Index));
            }
            return View(specie);
        }

        // GET: Specie/Delete/5
        public async Task<IActionResult> Delete(int id)
        {
            if (await _specieRepository.GetById(id) is Specie specie)
                return View(specie);

            return NotFound();
        }

        // POST: Specie/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (await _specieRepository.GetById(id) is Specie specie)
                await _specieRepository.Delete(specie);

            return RedirectToAction(nameof(Index));
        }
    }
}
