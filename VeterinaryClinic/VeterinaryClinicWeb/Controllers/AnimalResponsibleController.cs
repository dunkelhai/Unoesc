using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using VeterinaryClinic.BL;
using VeterinaryClinicWeb.Data;
using VeterinaryClinicWeb.Extensions;
using VeterinaryClinicWeb.Models.EF.Interfaces;

namespace VeterinaryClinicWeb.Controllers
{
    public class AnimalResponsibleController : Controller
    {
        private readonly IAnimalResponsibleRepository _animalResponsibleRepository;
        public AnimalResponsibleController(IAnimalResponsibleRepository animalResponsibleRepository)
        {
            _animalResponsibleRepository = animalResponsibleRepository;
        }

        // GET: AnimalResponsible
        public async Task<IActionResult> Index() =>
            View(await _animalResponsibleRepository.GetAll());

        // GET: AnimalResponsible/Details/5
        public async Task<IActionResult> Details(int id)
        {
            if (await _animalResponsibleRepository.GetById(id) is AnimalResponsible animalResponsible)
                return View(animalResponsible);
            return NotFound();
        }

        // GET: AnimalResponsible/Create
        public IActionResult Create()
        {
            ViewBag.GenderList = EnumExtensions.GetSelectList<Gender>();
            return View();
        }

        // POST: AnimalResponsible/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Name,CPF,Email,Phone,Gender")] AnimalResponsible animalResponsible)
        {
            if (ModelState.IsValid)
            {
                await _animalResponsibleRepository.Add(animalResponsible);
                return RedirectToAction(nameof(Index));
            }
            return View(animalResponsible);
        }

        // GET: AnimalResponsible/Edit/5
        public async Task<IActionResult> Edit(int id)
        {
            if (await _animalResponsibleRepository.GetById(id) is AnimalResponsible animalResponsible)
            {
                ViewBag.GenderList = EnumExtensions.GetSelectList<Gender>(animalResponsible.Gender);
                return View(animalResponsible);
            }
            return NotFound();
        }

        // POST: AnimalResponsible/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to.
        // For more details, see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Name,CPF,Email,Phone,Gender")] AnimalResponsible animalResponsible)
        {
            if (id != animalResponsible.Id)
                return NotFound();

            if (ModelState.IsValid)
            {
                try
                {
                    await _animalResponsibleRepository.Update(animalResponsible);
                }
                catch (DbUpdateConcurrencyException)
                {
                    throw;
                }
                return RedirectToAction(nameof(Index));
            }
            return View(animalResponsible);
        }

        // GET: AnimalResponsible/Delete/5
        public async Task<IActionResult> Delete(int id)
        {
            if(await _animalResponsibleRepository.GetById(id) is AnimalResponsible animalResponsible)
                return View(animalResponsible);

            return NotFound();
        }

        // POST: AnimalResponsible/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            if (await _animalResponsibleRepository.GetById(id) is AnimalResponsible animalResponsible)
                await _animalResponsibleRepository.Delete(animalResponsible);

            return RedirectToAction(nameof(Index));
        }
    }
}
